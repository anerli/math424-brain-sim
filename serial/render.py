import pyglet

from instant_neuron import Neuron, Synapse

import numpy as np

# class NeuronRenderer:
#     radius = 20
#     color = (50, 225, 30)

#     def draw(self, x, y, batch=None):
#         # TODO: Show voltage in an inner circle or something
#         circle = pyglet.shapes.Circle(x, y, radius=NeuronRenderer.radius, color=NeuronRenderer.color, batch=batch)
#         circle.draw()

# class SynapseRenderer:
#     pass

def dist(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

def direction(x1, x2, y1, y2):
    diff_x = x2-x1
    diff_y = y2-y1
    size = dist(0, 0, diff_x, diff_y)
    return diff_x / size, diff_y / size

def render_neuron(neuron: Neuron, radius, color):#, batch):
    #circle = pyglet.shapes.Circle(neuron.x, neuron.y, radius=radius, color=color)#, batch=batch)
    fill = int(255*(neuron.voltage / neuron.threshold))
    circle = pyglet.shapes.Circle(neuron.x, neuron.y, radius=radius, color=(255, 255-fill, 255-fill))
    circle.draw()

def render_synapse(presynaptic: Neuron, synapse: Synapse, color=(255, 255, 255)):#, batch):
    start_x = presynaptic.x
    start_y = presynaptic.y
    end_x = synapse.psn.x
    end_y = synapse.psn.y
    line = pyglet.shapes.Line(start_x, start_y, end_x, end_y, width=3, color=color)#, batch=batch)
    line.draw()

    start = np.array([start_x, start_y])
    end = np.array([end_x, end_y])

    norm = np.linalg.norm(end - start)

    normalized = (end - start) / norm

    arrow_len = 16
    arrow_width = 5

    p1 = np.array([end_x, end_y])
    perp = np.array([-normalized[1], normalized[0]])
    p2 = p1 - normalized*arrow_len + perp*arrow_width#np.cross(normalized, [0,1])*arrow_width
    p3 = p1 - normalized*arrow_len - perp*arrow_width#np.cross(normalized, [1,0])*arrow_width

    triangle = pyglet.shapes.Triangle(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], color=color)
    triangle.draw()