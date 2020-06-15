import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import random


class Model_one_NN:
    def __init__(self, file_name=None):
        if (file_name):
            self.model = keras.models.load_model(file_name)
        else:
            self.create_model()
            self.train_model()


    def train_model(self):
        f = open("config.txt", "r")
        content = f.readlines()
        f.close()
        x_train = []
        y_train = []
        x_test = []
        y_test = []
        #cpt = 0
        for line in content:
            line = line.strip("\n")
            tmp = line.split(":")
            if len(x_train) < ( len(content) * 0.8 ):                
                x_train.append(tmp[0].split("_"))
                y_train.append(tmp[1].split("_"))
            else:
                x_test.append(tmp[0].split("_"))
                y_test.append(tmp[1].split("_"))


        x_train = np.array(x_train)
        y_train = np.array(y_train)
        x_test = np.array(x_test)
        y_test = np.array(y_test)
        x_train=np.asfarray(x_train,int)
        x_test=np.asfarray(x_test,int)
        y_train=np.asfarray(y_train,float)
        y_test=np.asfarray(y_test,float)

        self.model.fit(x=x_train, y=y_train, validation_data=(x_test, y_test), epochs=200, batch_size = 64, verbose = True)

        self.test_validation()
            

    def create_model(self):
        self.model = keras.Sequential([
            keras.layers.Dense(64, input_shape=(48,), activation='relu'),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(2, activation = 'linear')
        ])

        self.model.compile(optimizer='adam',
              loss="MSE", metrics=["MeanAbsoluteError"])

    def save(self):
        self.model.save('model.h5')

    def predict(self, state):
        return self.model.predict(state)

    def test_validation(self) :
        f = open("config.txt", "r")
        content = f.readlines()
        f.close()
        x_test = []
        y_test = []
        cpt = 0
        for line in content:            
            line = line.strip("\n")
            tmp = line.split(":")
            if cpt > ( len(content) * 0.8 ):                
                x_test.append(tmp[0].split("_"))
                y_test.append(tmp[1].split("_"))
            cpt += 1

        x_test = np.array(x_test)
        y_test = np.array(y_test)
        x_test=np.asfarray(x_test,int)
        y_test=np.asfarray(y_test,float)

        diff_poll = 0.0
        diff_sat = 0.0

        for i in range(0, len(x_test)) :
            r = self.model.predict(np.array([x_test[i]]))
            diff_poll += abs(r[0][0] - y_test[i][0])
            diff_sat += abs(r[0][1] - y_test[i][1])

        diff_poll = diff_poll / len(x_test)
        diff_sat = diff_sat / len(x_test)

        print("Poll : ", diff_poll)
        print("Sat : ", diff_sat)
