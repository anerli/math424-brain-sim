from mpi4py import MPI

'''
Example running:

mpiexec -n 4 py test_mpi.py

Resources:

https://nyu-cds.github.io/python-mpi
'''

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print(f'I am thread {rank}')

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print('I got this data:', data)