from abc import ABC, abstractmethod
import random
from Algos import params, algo_tools
import numpy as np

# Interface d'un individu
class Individu(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def fitness(self):
        pass
    @abstractmethod
    def mutate(self, c):
        pass
    @abstractmethod
    def cross(self, i):
        pass

# Les mots de passe sont des individus
class Config(Individu):
    def __init__(self, model, config=None):
        super().__init__()
        self.model = model
        if(config!=None):
            self.config = config
        else:
            self.config = algo_tools.state_generator(params.CONFIG_SIZE)
        self.fitness_val = algo_tools.compute_result( self.model.predict(np.array( [self.config] ) ) )

    # La fitness est donnée par la similarité avec le bon mot de passe
    def fitness(self):
        return self.fitness_val

    # Fonction de mutation d'un mot de passe
    def mutate(self, p):
        i=0
        while i<len(self.config):
            tirage = random.random()
            if p >= tirage:
                self.config[i] = random.choice(params.CHARS)
            i += 1
        self.fitness_val = algo_tools.compute_result( self.model.predict( np.array( [self.config] ) ) )

    def cross_slice(self, c2):
        breakpoint = random.randrange(params.CONFIG_SIZE)
        crossed1 = self.config[:breakpoint] + c2.config[breakpoint:]
        crossed2 = c2.config[:breakpoint] + self.config[breakpoint:]
        return (Config(self.model, crossed1), Config(self.model, crossed2))

    def cross_merge(self, c2):
        crossed1 = []
        crossed2 = []
        for i in range(params.CONFIG_SIZE):

            if random.random() < 0.5:
                crossed1.append( self.config[i] )
                crossed2.append( c2.config[i] )
            else:
                crossed1.append( c2.config[i] )
                crossed2.append( self.config[i] )
        return (Config(self.model, crossed1), Config(self.model, crossed2))


    # On utilise la fonction de sélection définie dans params
    CROSS_FUNCTIONS = {
        "slice": cross_slice,
        "merge": cross_merge
    }
    # Fonction de cross-over de deux mots de passe
    def cross(self, p2):
        return self.CROSS_FUNCTIONS[params.CROSS_FUNCTION](self, p2)