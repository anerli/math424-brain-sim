from instant_neuron import *
from render import *
import random

def dist(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**(1/2)


def rand_dist_connect(neurons, Synapse: type, max_conn_dist=100):
    for n1 in neurons:
        for n2 in neurons:
            d = dist(n1.position, n2.position)
            if d > max_conn_dist:
                continue
            dist_ratio = d / max_conn_dist
            p = 1 - dist_ratio
            if random.random() < p:
                n1.connect(n2, Synapse)


class Brain:
    def __init__(self, neurons):
        self.neurons = neurons
        #self.renderers = renderers
        #self.N = Neuron
        #self.S = Synapse

    @classmethod
    def from_grid(cls, Neuron: type, Synapse: type, width, height, step_x, step_y):
        y = 0
        neurons = []
        while y < height:
            print(f'{y=}')
            x = 0
            while x < width:
                print(f'{x=}')
                n = Neuron()
                n.set_position(x, y)
                #rend = NeuronRenderer(n)
                #n.attach_renderer(rend)
                neurons.append(n)
                x += step_x
            y += step_y

        return cls(neurons)

        # Do random connections with probability based on distance between neurons
        # O(n^2)

    def draw(self, neuron_renderer: NeuronRenderer):
        n_batch = pyglet.graphics.Batch()
        for n in self.neurons:
            #n.draw()
            neuron_renderer.draw(n.x, n.y, n_batch)




# class DistBrain:
#     def __init__(self, Neuron: type, Synapse: type):


        