from src.AlgorithmThree import greedy_algorithm
from src.AdditionalFunctions import creating_outputfile

from time import time
import sys
from src.Scoring import count_points

if __name__ == "__main__":
    # result = algorithm("inputtext.txt")
    # print(result)


    # result = algorithm("charleston_road.in")
    # print(result)
    # connected = [i[2] for i in result]
    # result_list = [i[0] for i in result]
    # creating_outputfile(len(connected),[[i,0] for i in range(len(connected))],len(result),result_list)
    # val = count_points("algoroutput.txt", "charleston_road.in")
    # print(val)

    #
    # was = time()
    # result = algorithm("lets_go_higher.in")
    # print(time() - was)

    # result = algorithm("rue_de_londres.in")
    # print(result)
    # connected = [i[2] for i in result]
    # result_list = [i[0] for i in result]
    # creating_outputfile(len(connected),[[i,0] for i in range(len(connected))],len(result),result_list)
    # val = count_points("algoroutput.txt", "rue_de_londres.in")
    # print(val)

    # was = time()
    # result = algorithm("opera.in")
    # print(time() - was)
    #
    # was = time()
    # result = algorithm("rue_de_londres.in")
    #
    # print(time() - was)
    sys.setrecursionlimit(10000000)
    # was = time()
    # r = greedy_algorithm("charleston_road.in")
    # creating_outputfile(r[0], r[1], r[2], r[3])
    # val = count_points("algoroutput.txt", "charleston_road.in")
    # print(time() - was)
    # print(val)
    # was = time()
    # r = greedy_algorithm("lets_go_higher.in")
    # creating_outputfile(r[0], r[1], r[2], r[3])
    # val = count_points("algoroutput.txt", "lets_go_higher.in")
    # print(time() - was)
    # print(val)
    was = time()
    r = greedy_algorithm("../txt/opera.in")
    creating_outputfile(r[0], r[1], r[2], r[3])
    val = count_points("../txt/algoroutput.txt", "../txt/opera.in")
    print(time() - was)
    print(val)
    was = time()
    r = greedy_algorithm("rue_de_londres.in")
    creating_outputfile(r[0], r[1], r[2], r[3])
    val = count_points("../txt/algoroutput.txt", "../txt/rue_de_londres.in")
    print(time() - was)
    print(val)


