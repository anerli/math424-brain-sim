'''
Run:
mpiexec -n 6 python mpi_neurons.py
'''
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
        total_neurons=int(1e6),#4000000,
        total_connections=int(1e6),
    )

    # Make total neurons divisible by 6
    while config['total_neurons'] % comm.Get_size() != 0:
        config['total_neurons'] += 1

    # Generate random global connections
    global_connections = dict()
    for _ in range(config['total_connections']):
        valid = False
        while not valid:
            connection = (random.randrange(config['total_neurons']), random.randrange(config['total_neurons']))
            if connection[0] == connection[1] or connection in global_connections:
                valid = False
            else:
                #global_connections.add(connection)
                if connection[0] not in global_connections:
                    global_connections[connection[0]] = []
                global_connections[connection[0]].append(connection[1])
                valid = True
    #global_connections = list(global_connections)
    # FIXME: Isn't correct
    print('Num Global Connections:', len(global_connections))
else:
    config = None
    global_connections = None

config = comm.bcast(config, root=0)
global_connections = comm.bcast(global_connections, root=0)
#tprint(config)
# 2 threads: 666666
# 6 threads: 666667

num_neurons = config['total_neurons'] // comm.Get_size()
tprint('Number of neurons:', num_neurons)


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
    # for connection in global_connections:
    #     if get_global_idx(i) == connection[0]:
    #         neuron.connect(connection[1])
    neurons.append(neuron)

# Setup Connections From Globals
#for i in range(num_neurons):
    



#print(get_rank(100))

tprint(neurons[0])

#neurons[0].receive(200)

# Assumes d1 & d2 have same keys
def dictSumReduce(d1, d2, datatype):
    for key in d2:
        # if key not in d1:
        #     d1[key] = 0
        d1[key] += d2[key]
    return d1

dictSumOp = MPI.Op.Create(dictSumReduce, commute=True)

#while True:
for _ in range(1000000):
    update_start = time.time()

    neurons[0].receive(random.random()*100)

    # Maps global neuron indices to any changes in voltages
    updates = dict()
    for i in range(config['total_neurons']):
        updates[i] = 0
    # Update Loop
    for neuron in neurons:
        fired = neuron.update()
        if fired:
            tprint('Neuron', neuron, 'fired')
            for other_idx in neuron.connections:
                #if other_idx not in updates:
                #    updates[other_idx] = 0
                updates[other_idx] += neuron.threshold * neuron.voltage_forward_factor

    # Transmit updates
    #comm.barrier()
    updates = comm.allreduce(updates, op=dictSumOp)
    tprint('Size updates:', len(updates))


    update_time = time.time() - update_start
    tprint('Time to Update:', update_time, flush=True)
    #tprint(updates, flush=True)
    # root: the rank which recieves the result
    overall_update_time = comm.reduce(update_time, op=MPI.MAX, root=0)
    if rank == 0:
        print('Overall Time to Update:', overall_update_time)
    
    #comm.barrier()
    #time.sleep(1) # <- breaks mpi