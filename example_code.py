
updates = None
neurons = None
comm = None
dictSumOp = None

for neuron in neurons:
    fired = neuron.update()
    if fired:
        for other_idx in neuron.connections:
            if other_idx not in updates:
                updates[other_idx] = 0
                updates[other_idx] += neuron.threshold * neuron.voltage_forward_factor

updates = comm.allreduce(updates, op=dictSumOp)