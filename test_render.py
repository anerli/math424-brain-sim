from instant_neuron import *
from render import *
from brain import *
import pyglet

window = pyglet.window.Window(800, 600)

#nr = NeuronRenderer(100, 100)

b = Brain.from_grid(IAN, IES, 800, 600, 100, 100)
nr = NeuronRenderer()
print(len(b.neurons))

@window.event
def on_draw():
    window.clear()
    b.draw(nr)
    #nr.draw()

pyglet.app.run()
