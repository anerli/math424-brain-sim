
updates = None
neurons = None
comm = None
dictSumOp = None
MPI = None


def dictSumReduce(d1, d2, datatype):
    for key in d2:
        if key not in d1:
            d1[key] = 0
        d1[key] += d2[key]
    return d1

dictSumOp = MPI.Op.Create(dictSumReduce, commute=True)

for neuron in neurons:
    fired = neuron.update()
    if fired:
        for other_idx in neuron.connections:
            if other_idx not in updates:
                updates[other_idx] = 0
            updates[other_idx] += neuron.threshold * neuron.voltage_forward_factor

updates = comm.allreduce(updates, op=dictSumOp)