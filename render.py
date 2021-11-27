import pyglet

from instant_neuron import Neuron

class NeuronRenderer:
    radius = 20
    color = (50, 225, 30)
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y
    #def __init__(self, neuron: Neuron):
    #    self.neuron = neuron

    def draw(self, x, y, batch=None):
        # TODO: Show voltage in an inner circle or something
        circle = pyglet.shapes.Circle(x, y, radius=NeuronRenderer.radius, color=NeuronRenderer.color, batch=batch)
        circle.draw()

# class NeuronRenderer:
#     def __init__(self, radius=50, color=(50, 225, 30)):
#         self.radius = radius
#         self.color = color

#     def draw(self, x, y, v):
#         # TODO: Show voltage in an inner circle or something
#         circle = pyglet.shapes.Circle(x, y, radius=self.radius, color=self.color)
#         circle.draw()

class SynapseRenderer:
    pass