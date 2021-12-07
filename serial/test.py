from instant_neuron import *
from render import *
from brain import *

width=800
height=600

brain = Brain.from_grid(IAN, IES, width, height, 100, 100)
#nr = NeuronRenderer()
print(len(brain.neurons))


# while True:
#     for neuron in brain.neurons:
#         neuron.receive(50)
#         print(neuron)

brain.neurons[0].receive(200)

print(brain.neurons)