from ReadingData import reading_input_data
from Scoring import count_points
from AdditionalFunctions import nowalls
from Visualisation import text_connectedcells_visualization

from itertools import combinations


def finding_most_valid_routers(inputfilename):
    """
    :param inputfilename: The name of our input data file
    :return: List of possible placed routers with coordinates as a first param, coverage as second and distance to
    backbone as third
    """
    def calc_dist(backbone, router):
        return max(abs(backbone[0] - router[0]), abs(backbone[1] - router[1]))

    rows, cols, radius, connecting_to_backbone_cost, router_cost, budget,\
                                            initial_backbone, cells_list = reading_input_data(inputfilename)

    routers_list = list()
    i = 0

    for X in range(rows):
        for Y in range(cols):
            distance = calc_dist(initial_backbone, (X,Y))
            if distance != 0 and cells_list[X][Y] == ".":  #Adding routers that are not backbone pos and in . pos
                routers_list.append([(X,Y),0,distance])
            #Finding the coverage of our router
                for x in range(-radius, radius + 1):
                    for y in range(-radius, radius + 1):
                        try:
                            if x == 0 and y == 0:
                                continue
                            if cells_list[X + x][Y + y] == "." and X+x >=0 and Y+y>=0 and nowalls(cells_list, X, Y, X + x, Y + y):
                                routers_list[i][1] += 1
                        except IndexError:
                            pass
                i += 1

    return routers_list


def creating_outputfile(connected_cells, connected_cells_list, placed_routers,  routers_list):
    """
    :param connected_cells: Quantity of cell that are connected to the backbone
    :param connected_cells_list: List of cell that are connected to the backbone
    :param placed_routers:  Quantity of routers
    :param routers_list: List of routers
    """
    with open("algoroutput.txt","w") as file:
        file.write(str(connected_cells))
        file.write("\n")
        for i in connected_cells_list:
            file.write(str(i[0]) + " " + str(i[1])+ "\n")
        file.write(str(placed_routers))
        file.write("\n")
        for i in routers_list:
            file.write(str(i[0]) + " " + str(i[1])+ "\n")


def algorithm(routers_list):
    l = lambda x:(x[3], x[4], x[5])
    connecting_to_backbone_cost, router_cost, budget = l(reading_input_data("inputtext.txt"))

    total_cost = 0
    score_list_ = list()

    for len_ in range(1, budget // router_cost + 1):
        for subset in combinations(routers_list, len_):
            for i in subset:
                total_cost += (i[2] * connecting_to_backbone_cost + router_cost)

            if total_cost < budget:
                total_connected_cells = sum([i[2] for i in subset])
                ZAGLUSHKA_CELLS = [[i for i in range(2)] for j in range(total_connected_cells)]
                coordinates_of_routers = [i[0] for i in subset]

                creating_outputfile(total_connected_cells, ZAGLUSHKA_CELLS, len(subset), coordinates_of_routers)

                val = count_points("algoroutput.txt","inputtext.txt")
                if val == 54009:
                    c = text_connectedcells_visualization("algoroutput.txt","inputtext.txt")[0]
                    for i in c:
                        print("".join(i))

                score_list_.append(val)

            total_cost = 0

    return max(score_list_)







if __name__ == '__main__':
    routers_list = finding_most_valid_routers("inputtext.txt")
    # print(routers_list)
    print(algorithm(routers_list))
    #print(routers_list)
    # knapsack(routers_list,budget)
