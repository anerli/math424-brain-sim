from instant_neuron import *
from render import *
from brain import *
import time

import random



brain = Brain.from_grid(IAN, IES, 1000, 1000, 20, 20, max_conn_dist=40)
#nr = NeuronRenderer()
print('Number of neurons:', len(brain.neurons))
num_connections = 0
for n in brain.neurons:
    num_connections += len(n.connections)
print('Number of connections:', num_connections)


def update():
    start = time.time()

    brain.neurons[0].receive(random.random()*50)
    
    for neuron in brain.neurons:
        neuron.update()

    print('Time to update:', time.time() - start)

while True:
    update()

