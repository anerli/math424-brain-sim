from instant_neuron import *
from render import *
from brain import *
import pyglet

import random

width=800
height=600
window = pyglet.window.Window(width, height)

#nr = NeuronRenderer(100, 100)

brain = Brain.from_grid(IAN, IES, width, height, 100, 100)
#nr = NeuronRenderer()
print(len(brain.neurons))

@window.event
def on_draw():
    print('Drawing')

    

    # if random.random() < 0.5:
    #     brain.neurons[0].receive(50)
    #     print(brain.neurons[0])

    window.clear()

    for neuron in brain.neurons:
        render_neuron(neuron, 10, (50, 225, 30))

    for neuron in brain.neurons:
        if neuron.just_fired:
            synapse_color = (255, 0, 0)
        else:
            synapse_color = (255, 255, 255)
        for synapse in neuron.connections:
            
            render_synapse(neuron, synapse, color=synapse_color)
    
def update(dt):
    print('Updating')
    for neuron in brain.neurons:
        neuron.receive(2)

    for neuron in brain.neurons:
        neuron.update()


pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
