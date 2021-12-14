## Dependencies
- MPI (mpiexec)
- Python >=3.6
- mpi4py
- matplotlib
- pandas

## How to Run

Run simulation with 6 processes:
```
mpiexec -n 6 python mpi_neurons.py
```

Specifying the log file name:
```
mpiexec -n 6 python mpi_neurons.py 6p.csv
```

## Viewing Log Results
```
python view_logs.py
```