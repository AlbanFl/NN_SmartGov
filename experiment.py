import numpy as np
from Models import model_one_NN

model = model_one_NN.Model_one_NN("model.h5")
state = [0, 2, 3, 1, 5, 5, 4, 2, 3, 2, 5, 0, 1, 4, 5, 4, 3, 5, 4, 5, 3, 3, 3, 4, 2, 0, 2, 5, 0, 5, 3, 0, 3, 3, 1, 1, 4, 5, 0, 2, 5, 0, 1, 3, 4, 5, 5, 4]
r = model.predict(np.array( [state] ))
print(r)

'''
model = model_one_NN.Model_one_NN("model.h5")
algo = random_search.Random_search(model, 48)
f = open("test.txt", "a")
time = 5
algo.search(time)
result = algo.get_best_configs(100)
algo.clean_memory()
for i in range (0, len(result)):
    f.write(str(time) + " " + str(result[i][2]) + str(result[i][0]) + "\n")

from keras.models import Sequential
from keras.layers import Dropout, Dense
import tensorflow as tf
import numpy as np
import talos


def create_dataset():
    f = open("config.txt", "r")
    content = f.readlines()
    f.close()

    x = []
    y = []
    #cpt = 0
    for line in content:
        line = line.strip("\n")
        tmp = line.split(":")
        x.append(tmp[0].split("_"))
        y.append(tmp[1].split("_"))
        #y[cpt][0] = float(y[cpt][0]) / 500
        #y[cpt][1] = float(y[cpt][1]) / 500
        #cpt += 1


    x = np.array(x)
    y = np.array(y)
    x=np.asfarray(x,int)
    y=np.asfarray(y,float)

    return x,y

def simulation_model(x_train, y_train, x_val, y_val, params):

    model = Sequential()
    model.add(Dense(params['first_neuron'], input_dim=x_train.shape[1],
                    activation=params['activation'],
                    kernel_initializer=params['kernel_initializer']))
    
    model.add(Dropout(params['dropout']))

    model.add(Dense(2, activation='linear',
                    kernel_initializer=tf.keras.initializers.RandomNormal(mean=50.0, stddev=50.0, seed=None)))
    
    model.compile(loss=params['losses'],
                  optimizer=params['optimizer'],
                  metrics=['loss', talos.utils.metrics.f1score])
    
    history = model.fit(x_train, y_train, 
                        validation_data=[x_val, y_val],
                        batch_size=params['batch_size'],
                        callbacks=[talos.utils.live()],
                        epochs=params['epochs'],
                        verbose=0)

    return history, model
    '''