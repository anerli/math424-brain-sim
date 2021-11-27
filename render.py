import pyglet

class NeuronRenderer:
    radius = 100
    color = (50, 225, 30)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        # TODO: Show voltage in an inner circle or something
        circle = pyglet.shapes.Circle(self.x, self.y, radius=NeuronRenderer.radius, color=NeuronRenderer.color)
        circle.draw()

class SynapseRenderer:
    pass