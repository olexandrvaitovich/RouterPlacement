from src.AdditionalFunctions import finding_most_valid_routers, creating_outputfile, calc_dist
from src.ReadingData import reading_input_data
from src.Scoring import count_points

from random import choice

def algorithm(inputfilename):
    routers_list = finding_most_valid_routers(inputfilename)
    l = lambda x:(x[0],x[2],x[3], x[4], x[5], x[6])
    rows, radius, connecting_to_backbone_cost, router_cost, budget, initial_backbone = l(reading_input_data(inputfilename))


    placed_routers = list()
    while budget - router_cost > (rows*connecting_to_backbone_cost)/2 and len(routers_list) > 0:
        current = choice(routers_list)
        while True:
            val = find_better_neighbors(routers_list, current, initial_backbone, inputfilename)
            if current != val:
                current = val
            else:
                break

        routers_list = [i for i in routers_list if not(abs(i[0][0] - current[0][0]) <= radius and abs(i[0][1] - current[0][1]) <= radius)]
        placed_routers.append(current)
        budget -= current[2] * connecting_to_backbone_cost + router_cost

    return placed_routers


def find_better_neighbors(routers_list, current, initial_backbone, inputfilename):
    states_list = list()
    for i in routers_list:
        #print(i[0], initial_backbone)
        if abs(i[0][0] - current[0][0]) > 2 and abs(i[0][1] - current[0][1]) > 2:
            break
        if isatached(current, i):
            distance_to_backbone = calc_dist(initial_backbone, i[0])
            ZAGLUSHKA_CELLS = [[i for i in range(2)] for j in range(distance_to_backbone)]
            creating_outputfile(distance_to_backbone, ZAGLUSHKA_CELLS, 1, [i[0]])
            states_list.append((count_points("../txt/algoroutput.txt",inputfilename),i[0], None, distance_to_backbone,None))
                                                            #find_connected_tobackbone_cells(initial_backbone,i[0])))

    return max(states_list, key=lambda x: x[0])[1:] if len(states_list) != 0 else current


def isatached(cell1,cell2):
    return True if abs(cell1[0][0] - cell2[0][0]) <= 1 and  abs(cell1[0][1] - cell2[0][1]) <= 1 else False
