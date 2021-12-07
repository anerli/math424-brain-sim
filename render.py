import pyglet

from instant_neuron import Neuron

# class NeuronRenderer:
#     radius = 20
#     color = (50, 225, 30)

#     def draw(self, x, y, batch=None):
#         # TODO: Show voltage in an inner circle or something
#         circle = pyglet.shapes.Circle(x, y, radius=NeuronRenderer.radius, color=NeuronRenderer.color, batch=batch)
#         circle.draw()

# class SynapseRenderer:
#     pass

def render_neuron(neuron: Neuron, radius, color, batch):
    circle = pyglet.shapes.Circle(neuron.x, neuron.y, radius=radius, color=color, batch=batch)
    circle.draw()