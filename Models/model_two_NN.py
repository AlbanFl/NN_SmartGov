import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import random


class Model_two_NN:
    def __init__(self, filePollution=None, fileSatisfaction=None):
        if (filePollution and fileSatisfaction):
            self.modelPoll = keras.models.load_model(filePollution)
            self.modelSat = keras.models.load_model(fileSatisfaction)
        else:
            self.create_model()
            self.train_model()


    def train_model(self):
        f = open("config.txt", "r")
        content = f.readlines()
        f.close()

        x = []
        y_poll = []
        y_sat = []

        for line in content:
            line = line.strip("\n")
            tmp = line.split(":")
            x.append(tmp[0].split("_"))
            y_poll.append(tmp[1].split("_")[0])
            y_sat.append(tmp[1].split("_")[1])

        x = np.array(x)
        y_poll = np.array(y_poll)
        y_sat = np.array(y_sat)
        x=np.asfarray(x,int)
        y_poll=np.asfarray(y_poll,float)
        y_sat=np.asfarray(y_sat,float)

        self.modelPoll.fit(x, y_poll, validation_split = 0.2, epochs=1500, batch_size = 30, verbose = True)
        self.modelSat.fit(x, y_sat, validation_split = 0.2, epochs=1500, batch_size = 30, verbose = True)


    def create_model(self):
        self.modelPoll = keras.Sequential([
            keras.layers.Dense(75, input_shape =(48,) ,activation='relu'),
            keras.layers.Dense(50, activation='relu'),
            keras.layers.Dense(1, activation = 'linear')
        ])

        self.modelPoll.compile(optimizer='adam',
              loss=tf.keras.losses.MeanAbsoluteError(), lr = 0.01)

        self.modelSat = keras.Sequential([
            keras.layers.Dense(75, input_shape =(48,) ,activation='relu'),
            keras.layers.Dense(50, activation='relu'),
            keras.layers.Dense(1, activation = 'linear')
        ])

        self.modelSat.compile(optimizer='adam',
              loss=tf.keras.losses.MeanAbsoluteError(), lr = 0.01)


    def save(self):
        self.modelPoll.save('modelpoll.h5')
        self.modelSat.save('modelSat.h5')

    def predict(self, state):
        result = []
        result.append( self.modelPoll.predict(state)[0][0] )
        result.append( self.modelSat.predict(state)[0][0] )
        return [result]