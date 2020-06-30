# SmartGovNN

Smart Gov NN is used to learn best configurations of [SmartGovLezModel](https://github.com/AlbanFl/SmartGovLezModel). SmartGovLezModel, if used with [Result Generator Task](https://github.com/AlbanFl/SmartGovLezModel/tree/master/Extended_doc#result-generator-run) will create a file with configs and their results. These datas can be used to create a neural network in order to predict the results of new configurations.

## Requirements

To use this tool, you need to have :
- Python
- Tensorflow
- Keras

## How to use it

Once your file created by SmartGovLezModel, you have to train your neural network. You can also use the file `config.txt` that contains the results of around 86 000 simulations. To train your model :

`python main.py -t <file>`

The file in argument is the one with the configurations and the results. It will create a new file `model.h5` in your repository, which contains your newly trained neural network.
Once your neural network is trained, you can use it to find the best configurations with a genetic algorithm :

`python main.py -u <file>`

The file in argument is the one containing your neural network (probably `model.h5` if you did not rename it). It will load the neural network, and then launch a the research of best configurations using genetic algorithm for 60s.