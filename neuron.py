from typing import List
import itertools

# Instantaneous Action Neuron
class Neuron:
    resting = 0
    threshold = 100
    linear_decay = 1
    voltage_forward_factor = 0.25

    #id_iter = itertools.count()

    def __init__(self):
        self.connections = []
        self.voltage = self.resting
        #self.id = next(self.id_iter)
        # Firing only on update cycles prevents infinite depth problems
        self.fire_on_update = False

    def connect(self, other_idx):
        self.connections.append(other_idx)

    # def fire(self):
    #     for synapse in self.connections:
    #         synapse.fire(self.threshold)

    # Receive voltage v from a synapse
    def receive(self, v):
        self.voltage += v
        if self.voltage >= self.threshold:
            self.fire_on_update = True
            self.voltage = 0

    # Returns a dict mapping indices to changes in voltages
    def update(self):
        if self.fire_on_update:
            #self.fire()
            self.fire_on_update = False
        else:
            # Decay voltage to resting linearly
            self.voltage = max(self.resting, self.voltage - self.linear_decay)

    def __repr__(self):
        s = f'<Neuron voltage={self.voltage} connections={len(self.connections)}>'
        return s



# Instantaneous Electrical Synapse
# class Synapse:
#     voltage_forward_factor = 0.25
#     def __init__(self, postsynaptic_neuron_idx):
#         self.psn_idx = postsynaptic_neuron_idx

    # def fire(self, v):
    #     self.psn.receive(v * self.voltage_forward_factor)