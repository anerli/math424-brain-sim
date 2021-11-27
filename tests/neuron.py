from dataclasses import dataclass
from typing import ClassVar, List
from enum import Enum, auto
from math import sign

class NeuronState(Enum):
    RESTING: auto()
    DEPOLARIZING: auto()
    REPOLARIZING: auto()
    HYPERPOLARIZING: auto()

# Neuron Parameters
# "Real" things
RESTING_mV = -70.0
THRESHOLD_mV = -55.0
PEAK_POTENTIAL_mV = 40.0 # or 30.0? idk

# "Made up" things
#RESTING_DECAY_RATE = 0.1

def pp_func(potential):
    # Potassium pump function
    # Returns new potential after one time iteration
    diff = abs(potential - RESTING_mV)
    diff -= max(0, diff - 0.5) # Made up number
    



@dataclass
class Neuron:
    # == Class Variables ==
    # resting: ClassVar[float] = -70.0
    # threshold: ClassVar[float] = -55.0
    # peak_potential: 40.0 

    # == Neuron Properties ==
    neighbors: List['Neuron']
    potential: float = RESTING_mV # mV
    state: NeuronState = NeuronState.RESTING

    # Transfer voltage v to neighbors
    def forward(self, voltage):
        # Arbitrary algorithm: Actual transfer depends on synapses, synapse type (chemical vs electrical), etc.
        self.potential -= voltage
        amt = voltage / len(self.neighbors)
        for neuron in self.neighbors:
            neuron.potential += amt

    def step(self):
        if self.state == NeuronState.RESTING:
            if self.potential > self.threshold:
                self.state = NeuronState.DEPOLARIZING
            
        # No matter what, the potassium pump moves potential towards resting
        # This algorithm however, is somewhat arbitrary



