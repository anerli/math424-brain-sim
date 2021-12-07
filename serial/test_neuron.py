from instant_neuron import *

n1 = IAN()
n2 = IAN()

n1.connect(n2, IES)

neurons = [n1, n2]

for neuron in neurons:
    print(neuron)

for _ in range(20):
    n1.recieve(10)
    for neuron in neurons:
        neuron.update()
    for neuron in neurons:
        print(neuron)