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
        self.fire_on_update = False
        self.just_fired = False
        #self.renderer = None
        #self.position = None

    def connect(self, other: Neuron, Synapse: type):
        self.connections.append(Synapse(other))

    # def attach_renderer(self, renderer: NeuronRenderer):
    #     self.renderer = renderer

    # Neuron position useful mostly for renderer
    def set_position(self, x, y):
        #self.position = dict(x=x, y=y)
        self.x = x
        self.y = y

    def fire(self):
        for synapse in self.connections:
            synapse.fire(self.threshold)

    # Receive voltage v from a synapse
    def receive(self, v):
        self.voltage += v
        if self.voltage >= self.threshold:
            #self.fire()
            self.fire_on_update = True
            self.voltage = 0

    def update(self):
        self.just_fired = False
        if self.fire_on_update:
            self.fire()
            self.fire_on_update = False
            self.just_fired = True
        else:
            # Decay voltage to resting linearly
            self.voltage = max(IAN.resting, self.voltage - IAN.linear_decay)

    #def draw(self):
        # if self.renderer is None:
        #     raise Exception('Cannot draw neuron without attaching renderer.')
        # self.renderer.draw()

    def __repr__(self):
        s = f'<IAN_{self.id} voltage={self.voltage} connections={len(self.connections)}>'
        return s



# Instantaneous Electrical Synapse
class IES(Synapse):
    voltage_forward_factor = 0.2
    def __init__(self, postsynaptic_neuron):
        self.psn = postsynaptic_neuron

    def fire(self, v):
        self.psn.receive(v * IES.voltage_forward_factor)