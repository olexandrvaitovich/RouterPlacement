from LocalSearchAlgorithm import algorithm
from DumpAlgoritm import dump_algorithm
from AlgorithmTwo import dynamic_algorithm
from AlgorithmThree import greedy_algoritm
from AdditionalFunctions import finding_most_valid_routers

from time import time


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
    routers_list = finding_most_valid_routers("charleston_road.in")
    result = dynamic_algorithm(routers_list)
    print(time() - was)

    was = time()
    routers_list = finding_most_valid_routers("lets_go_higher.in")
    result = dynamic_algorithm(routers_list)
    print(time() - was)

    was = time()
    routers_list = finding_most_valid_routers("opera.in")
    result = dynamic_algorithm(routers_list)
    print(time() - was)

    was = time()
    routers_list = finding_most_valid_routers("opera.in")
    result = dynamic_algorithm(routers_list)
    print(time() - was)

