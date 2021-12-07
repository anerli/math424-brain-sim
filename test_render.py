from instant_neuron import *
from render import *
from brain import *
import pyglet

width=800
height=600
window = pyglet.window.Window(width, height)

#nr = NeuronRenderer(100, 100)

b = Brain.from_grid(IAN, IES, width, window, 100, 100)
nr = NeuronRenderer()
print(len(b.neurons))

@window.event
def on_draw():
    window.clear()
    b.draw(nr)
    #nr.draw()

pyglet.app.run()
