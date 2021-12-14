from mpi4py import MPI
import colors
from neuron import Neuron
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def tprint(*args, **kwargs):
    if rank > 5:
        print(*args, **kwargs)
        return
    tcolors = [colors.RED, colors.GREEN, colors.YELLOW, colors.BLUE, colors.MAGENTA, colors.CYAN]
    print(tcolors[rank], end='')
    print(*args, **kwargs, end='')
    print(colors.RESET)

tprint(f'I am thread {rank}')

if rank == 0:
    tprint('Number of threads:', comm.Get_size())
    # Communicate the total num neurons we want, etc
    config = dict(
        total_neurons=int(1e6),
        total_connections=int(1e7),
        total_stimulus=600
    )

    # Make total neurons divisible by 6
    while config['total_neurons'] % comm.Get_size() != 0:
        config['total_neurons'] += 1

    while config['total_stimulus'] % comm.Get_size() != 0:
        config['total_stimulus'] += 1

    # Generate random global connections
    global_connections = dict()
    for _ in range(config['total_connections']):
        valid = False
        while not valid:
            connection = (random.randrange(config['total_neurons']), random.randrange(config['total_neurons']))
            if connection[0] == connection[1] or connection in global_connections:
                valid = False
            else:
                if connection[0] not in global_connections:
                    global_connections[connection[0]] = []
                global_connections[connection[0]].append(connection[1])
                valid = True
else:
    config = None
    global_connections = None

config = comm.bcast(config, root=0)
global_connections = comm.bcast(global_connections, root=0)

num_neurons = config['total_neurons'] // comm.Get_size()
tprint('Number of neurons:', num_neurons)

num_stim = config['total_stimulus'] // comm.Get_size()
tprint('Num Stim:', num_stim)


# Get relative index within a process
def get_rel_idx(global_idx):
    return global_idx % num_neurons

def get_global_idx(rel_idx):
    return rel_idx + rank*num_neurons

def get_rank(global_idx):
    # Given the global idx of a neuron, return the rank of the thread which handles it
    relative_idx = get_rel_idx(global_idx)
    return (global_idx - relative_idx) // num_neurons

neurons = []
for i in range(num_neurons):
    neuron = Neuron()
    glob_idx = get_global_idx(i)
    if glob_idx in global_connections:
        for other_idx in global_connections[glob_idx]:
            neuron.connect(other_idx)
    neurons.append(neuron)


def dictSumReduce(d1, d2, datatype):
    for key in d2:
        if key not in d1:
            d1[key] = 0
        d1[key] += d2[key]
    return d1

dictSumOp = MPI.Op.Create(dictSumReduce, commute=True)

if rank == 0:
    num_fired_log = []
    update_time_log = []


for _ in range(1000):
    update_start = time.time()

    # Up to num_stim "stimulus" neurons which recieve random voltages automatically
    for i in range(min(num_stim, num_neurons)): neurons[i].receive(random.random()*100)

    # Maps global neuron indices to any changes in voltages
    updates = dict()

    # Update Loop
    num_fired = 0
    for neuron in neurons:
        fired = neuron.update()
        if fired:
            num_fired += 1
            #tprint('Neuron', neuron, 'fired')
            for other_idx in neuron.connections:
                if other_idx not in updates:
                    updates[other_idx] = 0
                updates[other_idx] += neuron.threshold * neuron.voltage_forward_factor

    # Transmit updates
    updates = comm.allreduce(updates, op=dictSumOp)

    # Transfer updates to this process
    for rel_idx, neuron in enumerate(neurons):
        glob_idx = get_global_idx(rel_idx)
        if glob_idx in updates:
            neuron.receive(updates[glob_idx])

    update_time = time.time() - update_start
    #tprint('Time to Update:', update_time, flush=True)
    #tprint(updates, flush=True)
    # root: the rank which recieves the result
    total_num_fired = comm.reduce(num_fired, op=MPI.SUM, root=0)
    overall_update_time = comm.reduce(update_time, op=MPI.MAX, root=0)
    if rank == 0:
        print('Number of Neurons Fired this Update:', total_num_fired)
        print('Overall Time to Update:', overall_update_time, flush=True)
        num_fired_log.append(total_num_fired)
        update_time_log.append(overall_update_time)

if rank == 0:
    import pandas as pd
    import sys
    df = pd.DataFrame(list(zip(update_time_log, num_fired_log)), columns=['UpdateTime', 'NeuronsFired'])

    fname = 'log.csv'
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    df.to_csv(fname)
