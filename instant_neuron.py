from typing import List
import itertools

# Base Neuron Class
class Neuron:
    pass

# Base Synapse Class
class Synapse:
    pass

# Instantaneous Action Neuron
class IAN(Neuron):
    resting = 0
    threshold = 100
    linear_decay = 1

    id_iter = itertools.count()

    def __init__(self):
        self.connections = []
        self.voltage = IAN.resting
        self.id = next(IAN.id_iter)

    def connect(self, other: Neuron, Synapse: type):
        self.connections.append(Synapse(other))

    def fire(self):
        for synapse in self.connections:
            synapse.fire(self.threshold)

    # Receive voltage v from a synapse
    def recieve(self, v):
        self.voltage += v
        if self.voltage >= self.threshold:
            self.fire()
            self.voltage = 0

    def update(self):
        # Decay voltage to resting linearly
        self.voltage = max(IAN.resting, self.voltage - IAN.linear_decay)

    def __repr__(self):
        s = f'<IAN_{self.id} voltage={self.voltage} connections={len(self.connections)}>'
        return s



# Instantaneous Electrical Synapse
class IES(Synapse):
    voltage_forward_factor = 0.5
    def __init__(self, postsynaptic_neuron):
        self.psn = postsynaptic_neuron

    def fire(self, v):
        self.psn.recieve(v * IES.voltage_forward_factor)