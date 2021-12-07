'''
Run:
mpiexec -n 6 python mpi_neurons.py
'''
from mpi4py import MPI
import colors

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
        total_neurons=100
    )

    # Make total neurons divisible by 6
    while config['total_neurons'] % comm.Get_size() != 0:
        config['total_neurons'] += 1
else:
    config = None

config = comm.bcast(config, root=0)

tprint(config)