'''
Run:
mpiexec -n 6 python mpi_neurons.py
'''
from mpi4py import MPI
import colors
from neuron import Neuron, Synapse

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
        total_neurons=100,
        total_connections=20,
    )

    # Make total neurons divisible by 6
    while config['total_neurons'] % comm.Get_size() != 0:
        config['total_neurons'] += 1
else:
    config = None

config = comm.bcast(config, root=0)

#tprint(config)

num_neurons = config['total_neurons'] // 6
#tprint(num_neurons)

def get_rank(idx):
    # Given the global idx of a neuron, return the rank of the thread which handles it
    relative_idx = idx % num_neurons
    return (idx - relative_idx) // num_neurons

neurons = []
for _ in range(num_neurons):
    neurons.append(Neuron())

#print(get_rank(100))

tprint(neurons[0])