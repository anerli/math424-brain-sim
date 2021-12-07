'''
Run:
mpiexec -n 6 python mpi_neurons.py
'''
from mpi4py import MPI
import colors
from neuron import Neuron
import time

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
        total_neurons=4000000,
        total_connections=20,
    )

    # Make total neurons divisible by 6
    while config['total_neurons'] % comm.Get_size() != 0:
        config['total_neurons'] += 1
else:
    config = None

config = comm.bcast(config, root=0)

#tprint(config)
# 2 threads: 666666
# 6 threads: 666667

num_neurons = config['total_neurons'] // comm.Get_size()
tprint('Number of neurons:', num_neurons)


# Get relative index within a process
def get_rel_idx(global_idx):
    return global_idx % num_neurons

def get_rank(global_idx):
    # Given the global idx of a neuron, return the rank of the thread which handles it
    relative_idx = get_rel_idx(global_idx)
    return (global_idx - relative_idx) // num_neurons

neurons = []
for _ in range(num_neurons):
    neurons.append(Neuron())

#print(get_rank(100))

tprint(neurons[0])

neurons[0].receive(200)

#while True:
for _ in range(1000000):
    update_start = time.time()
    # Maps global neuron indices to any changes in voltages
    updates = dict()
    # Update Loop
    for neuron in neurons:
        fired = neuron.update()
        if fired:
            for other_idx in neuron.connections:
                if other_idx not in updates:
                    updates[other_idx] = 0
                updates[other_idx] += neuron.threshold * neuron.voltage_forward_factor

    update_time = time.time() - update_start
    tprint('Time to Update:', update_time)
    tprint(updates, flush=True)

    # root: the rank which recieves the result
    overall_update_time = comm.reduce(update_time, op=MPI.MAX, root=0)
    if rank == 0:
        print('Overall Time to Update:', overall_update_time)
    #comm.barrier()
    #time.sleep(1) # <- breaks mpi