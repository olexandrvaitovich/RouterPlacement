from LocalSearchAlgorithm import algorithm
from DumpAlgoritm import dump_algorithm
from AlgorithmTwo import dynamic_algorithm
from AlgorithmThree import greedy_algorithm
from AdditionalFunctions import finding_most_valid_routers2, creating_outputfile

from time import time

from Scoring import count_points

if __name__ == "__main__":
    # result = dump_algorithm("inputtext.txt")
    # print(result)

    # was = time()
    # result = algorithm("charleston_road.in")
    # print(time() - was)
    #
    # was = time()
    # result = algorithm("lets_go_higher.in")
    # print(time() - was)
    #
    # was = time()
    # result = algorithm("opera.in")
    # print(time() - was)
    #
    # was = time()
    # result = algorithm("rue_de_londres.in")
    # print(time() - was)

    was = time()
    r = greedy_algorithm("charleston_road.in")
    creating_outputfile(r[0], r[1], r[2], r[3])
    val = count_points("algoroutput.txt", "charleston_road.in")
    print(time() - was)
    print(val)
    was = time()
    r = greedy_algorithm("lets_go_higher.in")
    creating_outputfile(r[0], r[1], r[2], r[3])
    val = count_points("algoroutput.txt", "lets_go_higher.in")
    print(time() - was)
    print(val)
    was = time()
    r = greedy_algorithm("opera.in")
    creating_outputfile(r[0], r[1], r[2], r[3])
    val = count_points("algoroutput.txt", "opera.in")
    print(time() - was)
    print(val)
    was = time()
    r = greedy_algorithm("rue_de_londres.in")
    creating_outputfile(r[0], r[1], r[2], r[3])
    val = count_points("algoroutput.txt", "rue_de_londres.in")
    print(time() - was)
    print(val)


