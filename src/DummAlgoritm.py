from src.ReadingData import reading_input_data
from src.Scoring import count_points
from src.AdditionalFunctions import finding_most_valid_routers, creating_outputfile

from itertools import combinations


def dumm_algorithm(inputfilename):
    routers_list = finding_most_valid_routers(inputfilename)
    l = lambda x:(x[3], x[4], x[5])
    connecting_to_backbone_cost, router_cost, budget = l(reading_input_data(inputfilename))

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

                val = count_points("../txt/algoroutput.txt", inputfilename)

                score_list_.append(val)

            total_cost = 0

    return max(score_list_)


if __name__ == '__main__':
    max_score = dumm_algorithm("../txt/charleston_road.in")