import random
import numpy as np
from Algos import params


def state_generator(nb_entry):
    state = []
    for i in range(0, nb_entry):
        state.append(random.randint(0,5))
    return state

def compute_result(elem):
    return ( ( params.base_pollution - elem[0][0] ) / 40) + (elem[0][1] / 10)