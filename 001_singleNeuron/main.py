# @ Author: Jakob Abou Zeid
# @ email: jakob.abouzeid@gmail.com


# We already assembled the dataset in our Jupyter Notebook and can just load it here.
import typing
in_type = NewType("Neuron", Neuron)
import numpy as np

class Neuron:
    next_neuron_ID = 0
    def __init__(self, inputs: typing.List[Neuron]) -> None:
        parameters = {}
        for input_val in inputs:
            parameters[input_val.neuron_ID] = np.random.rand()

        
        self.neuron_ID = Neuron.next_neuron_ID
        Neuron.next_neuron_ID +=1




