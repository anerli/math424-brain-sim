from typing import List
import itertools

# Instantaneous Action Neuron
class Neuron:
    resting = 0
    threshold = 100
    linear_decay = 1

    #id_iter = itertools.count()

    def __init__(self):
        self.connections = []
        self.voltage = self.resting
        #self.id = next(self.id_iter)
        # Firing only on update cycles prevents infinite depth problems
        self.fire_on_update = False

    def connect(self, other: 'Neuron', Synapse: type):
        self.connections.append(Synapse(other))

    def fire(self):
        for synapse in self.connections:
            synapse.fire(self.threshold)

    # Receive voltage v from a synapse
    def receive(self, v):
        self.voltage += v
        if self.voltage >= self.threshold:
            self.fire_on_update = True
            self.voltage = 0

    def update(self):
        if self.fire_on_update:
            self.fire()
            self.fire_on_update = False
        else:
            # Decay voltage to resting linearly
            self.voltage = max(self.resting, self.voltage - self.linear_decay)

    def __repr__(self):
        s = f'<IAN voltage={self.voltage} connections={len(self.connections)}>'
        return s



# Instantaneous Electrical Synapse
class Synapse:
    voltage_forward_factor = 0.25
    def __init__(self, postsynaptic_neuron):
        self.psn = postsynaptic_neuron

    def fire(self, v):
        self.psn.receive(v * self.voltage_forward_factor)