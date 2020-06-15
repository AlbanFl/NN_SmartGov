import random
import numpy as np
import time
from operator import itemgetter, attrgetter
from Algos import algo_tools

class Random_search:
    def __init__(self, model, nb_entry):
        self.model = model
        self.nb_entry = nb_entry
        self.memory = []

    def clean_memory(self):
        self.memory = []

    def search(self, nb_seconds):
        init_time = time.perf_counter()
        while time.perf_counter() - init_time < nb_seconds :
            state = algo_tools.state_generator(self.nb_entry)
            result = self.model.predict( np.array( [state] ))
            self.memory.append([state, result , algo_tools.compute_result(result)])
        print(len(self.memory))

    def get_memory(self):
        return self.memory

    def get_best_configs(self, nb_config):
        self.memory.sort(key= itemgetter(2), reverse=True)
        return self.memory[:nb_config]