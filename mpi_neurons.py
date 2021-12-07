'''
Run:
mpiexec -n 6 python mpi_neurons.py
'''
from mpi4py import MPI
import colors

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def tprint(*args, **kwargs):
    tcolors = [colors.RED, colors.GREEN, colors.YELLOW, colors.BLUE, colors.MAGENTA, colors.CYAN]
    print(tcolors[rank], end='')
    print(*args, **kwargs)
    print(colors.RESET, end='')

tprint(f'I am thread {rank}')

if rank == 0:
    # Communicate the total num neurons we want, etc
    pass