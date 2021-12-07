from instant_neuron import *
from render import *
from brain import *
import pyglet

width=800
height=600
window = pyglet.window.Window(width, height)

#nr = NeuronRenderer(100, 100)

brain = Brain.from_grid(IAN, IES, width, height, 100, 100)
#nr = NeuronRenderer()
print(len(brain.neurons))

@window.event
def on_draw():
    window.clear()
    #batch = pyglet.graphics.Batch()
    for neuron in brain.neurons:
        render_neuron(neuron, 10, (50, 225, 30))#, batch)
    #batch.draw()
    #b.draw(nr)
    #nr.draw()

pyglet.app.run()
