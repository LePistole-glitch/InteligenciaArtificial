#8reinas
import random
import numpy
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
import matplotlib.pyplot as plt

#Paramtros del problema - Numero de reinas
NB_QUEENS = 4

def evalNQueens(individual):
    size = len(individual)
    #Los ataques solo pueden ser en digonales
    diagonal_izquierda_derecha = [0] * (2*size-1)
    diagonal_derecha_izquierda = [0] * (2*size-1)
    #Numero de reinas en cada diagonal
    for i in range(size):#recorrer columnas 
        diagonal_izquierda_derecha[i+individual[i]] += 1 #[col + fila]
        diagonal_derecha_izquierda[size-1-i+individual[i]] += 1
    #Numero de ataques en cada diagonal
    suma = 0
    for i in range(2*size-1): #recorrer todas las diagonales
        if diagonal_izquierda_derecha[i] > 1: #hay ataque
            suma += diagonal_izquierda_derecha[i] - 1 #n-1 ataques
        if diagonal_derecha_izquierda[i] > 1:
            suma += diagonal_derecha_izquierda[i] - 1
    
    return suma,

#Def del problema
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

#Registro de funciones
toolbox = base.Toolbox()
toolbox.register("permutation", random.sample, range(NB_QUEENS), NB_QUEENS)
#
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.permutation)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
#Funcon de evaluacion
toolbox.register("evaluate", evalNQueens)
#Ope Geneticos
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=2.0/NB_QUEENS)
toolbox.register("select", tools.selTournament, tournsize=3)

def main(): #funcion que genera la primera 
    seed = 0
    random.seed(seed)

    pop = toolbox.population(n=10) #10 Habitantes
    hof = tools.HallOfFame(1)     #Objeto q almaena el mejor individuo
    stats = tools.Statistics(lambda ind: ind.fitness.values) #calculamos el fittness

    stats.register("Avg", numpy.mean)
    stats.register("Std", numpy.std)
    stats.register("Min", numpy.min)
    stats.register("Max", numpy.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats,
                        halloffame=hof, verbose=True) #algoritmo genetco como "caja negra"

    return pop, stats, hof

if __name__ == "__main__":
    pop, stats, best = main()
    print(best)
    print(best[0].fitness.values)
    y = best[0]
    x = range(NB_QUEENS)
    x = numpy.array(x)
    print(x)
    y = numpy.array(y)
    print(y)
    x = x + 0.5
    y = y + 0.5
    plt.figure()
    plt.scatter(x, y)
    plt.xlim(0,NB_QUEENS)
    plt.ylim(0,NB_QUEENS)
    plt.xticks(x-0.5)
    plt.yticks(y-0.5)
    plt.grid(True)
    plt.title(u"Mejor Individuo")
    plt.show()