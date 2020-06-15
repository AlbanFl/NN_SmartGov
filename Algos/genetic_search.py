import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MaxNLocator
from Algos import Individu, Population, params
from Algos.Individu import Config, Individu
from Algos.Population import Population
import sys
import time
import argparse
import json


def updateParams(p):
    params.GROUP_ID = p["GROUP_ID"]
    params.N = p["N"]
    params.N_ENV2 = p["N_ENV2"]
    params.MIX_THRESHOLD = p["MIX_THRESHOLD"]
    params.MAXGEN = p["MAXGEN"]
    params.e = p["e"]
    params.p_cross = p["p_cross"]
    params.p_mut = p["p_mut"]
    params.SELECT_FUNCTION = p["SELECT_FUNCTION"]
    params.TOURNAMENT_SIZE = p["TOURNAMENT_SIZE"]
    params.TOURNAMENT_P = p["TOURNAMENT_P"]
    params.CROSS_FUNCTION = p["CROSS_FUNCTION"]
    params.n_test = p["n_test"]
def getParams():
    return {
        "GROUP_ID":params.GROUP_ID,
        "N":params.N,
        "N_ENV2":params.N_ENV2,
        "MIX_THRESHOLD":params.MIX_THRESHOLD,
        "MAXGEN":params.MAXGEN,
        "e":params.e,
        "p_cross":params.p_cross,
        "p_mut":params.p_mut,
        "SELECT_FUNCTION":params.SELECT_FUNCTION,
        "TOURNAMENT_SIZE":params.TOURNAMENT_SIZE,
        "TOURNAMENT_P":params.TOURNAMENT_P,
        "CROSS_FUNCTION":params.CROSS_FUNCTION,
        "n_test":params.n_test
    }

class Algo:
    def __init__(self, model):
        self.pop = Population(Config, params.N, model)
        self.index = 0
        self.t = 0
        self.x_vals = [self.index]
        self.best_vals = [self.pop.best.fitness()]
        self.mean_vals = [self.pop.fitsum/params.N]
        self.done = False

    def step(self):
        self.index += 1
        self.x_vals.append(self.index)
        t_0 = time.time()
        out = self.pop.nextGen()
        self.t += time.time() - t_0
        self.best_vals.append(out[0])
        self.mean_vals.append(out[1])
            
    def results(self):
        res = {
            "group_id":params.GROUP_ID,
            "password":alg.pop.best.password if self.done else "",
            "best_fitness":alg.best_vals,
            "average_fitness":alg.mean_vals,
            "time":alg.t,
            "n_generations":alg.index,
            "found":self.done
        }
        return res

    def search(self, nb_seconds):
        init_time = time.perf_counter()
        while time.perf_counter() - init_time < nb_seconds :
            self.step()
        print("Nombre de générations : " + str(self.index))
        
    def get_best_configs(self, nb_configs):
        return self.pop.pop[:nb_configs]
        

'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument("--benchmark", action="store_true", help="Enregistre les résults")
    parser.add_argument("-p", "--params", action="store", help="Charge les paramètres à tester")
    args = parser.parse_args()

    benchmarks = []

    if(args.benchmark):
        if(args.params is None):
            benchmark_params = [getParams()]
            n_test = params.n_test
        else:
            benchmark_params = json.load(open(args.params, "r"))
            n_test = 0
            for t in benchmark_params:
                n_test += t["n_test"]
        pbar = tqdm(total=params.MAXGEN*n_test)
        for i in range(len(benchmark_params)):
            updateParams(benchmark_params[i])
            results_test = []
            for j in range(benchmark_params[i]["n_test"]):
                alg = Algo()
                while not(alg.done) and alg.index<params.MAXGEN:
                    alg.step()
                    pbar.update(1)
                pbar.total -= params.MAXGEN - alg.index
                results_test.append(alg.results())
            benchmarks.append({"params":benchmark_params[i], "results":results_test})
        f = open("results.json", "w")
        json.dump(benchmarks, f)
    else:
        plt.style.use("ggplot")
        alg = Algo()
        def animate(i):
            if(not(alg.done)):
                alg.step()
                sys.stdout.flush()
                l = (max(params.PASS_LENGTH) - len(alg.pop.best.password))
                sys.stdout.write("\r"+"|" + "."*5 + alg.pop.best.password + "*"*l + "."*3 + "|")
                # print(pop.best.password)
                plt.cla()

                if(alg.done):
                    sys.stdout.flush()
                    sys.stdout.write("\r"+"|" + "."*(4+l//2) + alg.pop.best.password + "."*(l//2) + "."*4 + "|\n")
                    print("|" + "-"*(8+max(params.PASS_LENGTH)) + "|")
                    print("Time : " + str(alg.t) + "s")
                    print("Number of generation : " + str(alg.index))
                    plt.scatter(alg.x_vals[alg.index], alg.best_vals[alg.index], marker="x")
                # plt.legend(loc="upper left")
                plt.plot(alg.x_vals, alg.best_vals, "crimson")
                plt.plot(alg.x_vals, alg.mean_vals, "tab:purple")
                plt.plot(alg.x_vals, alg.mean_vals2, "tab:cyan", linestyle=':')
                plt.gca().legend(("Best fitness", "Average fitness", "Average fitness (2nd population)"))
                plt.gcf().suptitle("Évolution de la fitness au cours des générations", fontsize=12)
                plt.xlabel("Génération")
                plt.ylabel("Fitness")

        print("|" + "-"*5 + "CRACKING THE CODE" + "-"*4 + "|")
        print("|" + "-"*(10+max(params.PASS_LENGTH) - 2) + "|")
        anim = animation.FuncAnimation(plt.gcf(), animate, interval=1)
        plt.gcf().canvas.set_window_title("password-gen")
        plt.show()

'''