import sys, getopt
import numpy as np

from Models import model_one_NN
from Models import model_two_NN
from Algos import random_search
from Algos import genetic_search
from Algos import algo_tools
import random
import json
from datetime import datetime

def benchmark_random(model):
    algo = random_search.Random_search(model, 48)
    f = open("result_random.txt", "a")
    nb_seconds = 660
    while nb_seconds <= 1200 :
        #time = random.randint(2,60)
        time = nb_seconds
        algo.search(time)
        result = algo.get_best_configs(5)
        algo.clean_memory()
        f.write(str(time) + " " + str(result[0][2]) + str(result[0][0]) + "\n")
        nb_seconds += 60
    f.close()

def benchmark_genetic(model):
    f = open("result_genetic.txt", "a")
    nb_seconds = 2
    while nb_seconds <= 90:
        algo = genetic_search.Algo(model)
        algo.search(nb_seconds)
        result = algo.get_best_configs(1)
        f.write(str(nb_seconds) + " " + str(result[0].fitness_val) + " " + str(result[0].config) + "\n")
        nb_seconds += 2
    f.close()

def genetic_algorithm(model, nb_seconds):
        algo = genetic_search.Algo(model)
        algo.search(nb_seconds)
        result = algo.get_best_configs(1)

        allSquare = [[ [ 45.43, 4.4 ], [ 45.609, 4.4 ], [ 45.609, 4.665 ], [ 45.43, 4.665 ] ],
            [ [ 45.609, 4.4 ], [ 45.788, 4.4 ], [ 45.788, 4.665 ], [ 45.609, 4.665 ] ],
            [ [ 45.788, 4.4 ], [ 45.967, 4.4 ], [ 45.967, 4.665 ], [ 45.788, 4.665 ] ],
            [ [ 45.967, 4.4 ], [ 46.146, 4.4 ], [ 46.146, 4.665 ], [ 45.967, 4.665 ] ],
            [ [ 45.43, 4.665 ], [ 45.609, 4.665 ], [ 45.609, 4.93 ], [ 45.43, 4.93 ] ],
            [ [ 45.609, 4.665 ], [ 45.788, 4.665 ], [ 45.788, 4.93 ], [ 45.609, 4.93 ] ],
            [ [ 45.788, 4.665 ], [ 45.967, 4.665 ], [ 45.967, 4.93 ], [ 45.788, 4.93 ] ],
            [ [ 45.967, 4.665 ], [ 46.146, 4.665 ], [ 46.146, 4.93 ], [ 45.967, 4.93 ] ],
            [ [ 45.43, 4.93 ], [ 45.609, 4.93 ], [ 45.609, 5.195 ], [ 45.43, 5.195 ] ],
            [ [ 45.609, 4.93 ], [ 45.788, 4.93 ], [ 45.788, 5.195 ], [ 45.609, 5.195 ] ],
            [ [ 45.788, 4.93 ], [ 45.967, 4.93 ], [ 45.967, 5.195 ], [ 45.788, 5.195 ] ],
            [ [ 45.967, 4.93 ], [ 46.146, 4.93 ], [ 46.146, 5.195 ], [ 45.967, 5.195 ] ],
            [ [ 45.43, 5.195 ], [ 45.609, 5.195 ], [ 45.609, 5.46 ], [ 45.43, 5.46 ] ],
            [ [ 45.609, 5.195 ], [ 45.788, 5.195 ], [ 45.788, 5.46 ], [ 45.609, 5.46 ] ],
            [ [ 45.788, 5.195 ], [ 45.967, 5.195 ], [ 45.967, 5.46 ], [ 45.788, 5.46 ] ],
            [ [ 45.967, 5.195 ], [ 46.146, 5.195 ], [ 46.146, 5.46 ], [ 45.967, 5.46 ] ],
            ]
        data = {}

        count = 0
        for i in range(len(result[0].config)): # Start counting from 1
            if i % 3 == 0:
                if (result[0].config[i]==0):
                    stringSurv = "NO_SURVEILLANCE"
                elif (result[0].config[i]==1):
                    stringSurv = "PATROL"
                elif (result[0].config[i]==2):
                    stringSurv = "CAMERA"
                elif (result[0].config[i]==3):
                    stringSurv = "BARRIER"
                elif (result[0].config[i]==4):
                    stringSurv = "CHEAP_TOLL"
                elif (result[0].config[i]==5):
                    stringSurv = "EXPENSIVE_TOLL"
                else :
                    print("error with surveillance")

                if (result[0].config[i+1]==0):
                    stringPrivCrit = "CRITAIR_1"
                elif (result[0].config[i+1]==1):
                    stringPrivCrit = "CRITAIR_2"
                elif (result[0].config[i+1]==2):
                    stringPrivCrit = "CRITAIR_3"
                elif (result[0].config[i+1]==3):
                    stringPrivCrit = "CRITAIR_4"
                elif (result[0].config[i+1]==4):
                    stringPrivCrit = "CRITAIR_5"
                elif (result[0].config[i+1]==5):
                    stringPrivCrit = "NONE"
                else :
                    print("error with private criteria")
                
                if (result[0].config[i+2]==0):
                    stringDeliCrit = "CRITAIR_1"
                elif (result[0].config[i+2]==1):
                    stringDeliCrit = "CRITAIR_2"
                elif (result[0].config[i+2]==2):
                    stringDeliCrit = "CRITAIR_3"
                elif (result[0].config[i+2]==3):
                    stringDeliCrit = "CRITAIR_4"
                elif (result[0].config[i+2]==4):
                    stringDeliCrit = "CRITAIR_5"
                elif (result[0].config[i+2]==5):
                    stringDeliCrit = "NONE"
                else :
                    print("error with deliveri criteria")

                squareNumber = str(count)
                data[squareNumber]= {}
                data[squareNumber]["perimeter"]= allSquare[count]
                count+=1
                data[squareNumber]["private criteria"]= stringPrivCrit
                data[squareNumber]["surveillance"]= stringSurv
                data[squareNumber]["delivery criteria"]= stringDeliCrit
    
        fileName = datetime.now().strftime("JSON/environment-%d-%m-%Y-%H-%M-%S.json")

        wfile = open(fileName, 'w')
        wfile.write(json.dumps(data, sort_keys=True, indent=4))
        wfile.close()


def main(argv):
    model = None
    try:
        opts, args = getopt.getopt(argv,"htu",["help", "train", "use", "experiment"])
    except getopt.GetoptError:
      print("Erreur d'arguments. Lancez script.py -h pour plus d'information.")
      sys.exit()
    for opt, arg in opts:
        if opt in ('-h', "-help"):
            print("Bienvenue dans l'aide de notre script")
            print("Si vous souhaitez entrainer un modele : main.py -train")
            print("Si vous souhaitez utiliser un modèle déjà entrainé : main.py -use")
            sys.exit()
        elif opt in ("-t", "-train"):
            #model = model_two_NN.Model_two_NN()
            model = model_one_NN.Model_one_NN()
            model.save()
    
    if model == None:
        #If we dont train it, then we load it from a file
        model = model_one_NN.Model_one_NN("model.h5")


    genetic_algorithm(model, 90)


if __name__ == "__main__":
    main(sys.argv[1:]) 