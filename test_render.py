from instant_neuron import *
from render import *
import pyglet

window = pyglet.window.Window(800, 600)

nr = NeuronRenderer(100, 100)

@window.event
def on_draw():
    window.clear()
    nr.draw()

pyglet.app.run()
