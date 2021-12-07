
updates = None
neurons = None

for neuron in neurons:
    fired = neuron.update()
    if fired:
        #tprint('Neuron', neuron, 'fired')
        for other_idx in neuron.connections:
            if other_idx not in updates:
                updates[other_idx] = 0
                updates[other_idx] += neuron.threshold * neuron.voltage_forward_factor

# Transmit updates
#comm.barrier()
updates = comm.allreduce(updates, op=dictSumOp)