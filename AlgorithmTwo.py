from AdditionalFunctions import nowalls
from ReadingData import reading_input_data
from Scoring import count_points
import copy


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
                routers_list.append([(X,Y),0,distance, set()])
            #Finding the coverage of our router
                for x in range(-radius, radius + 1):
                    for y in range(-radius, radius + 1):
                        try:
                            if x == 0 and y == 0:
                                continue
                            if cells_list[X + x][Y + y] == "." and X+x >=0 and Y+y>=0 and nowalls(cells_list, X, Y, X + x, Y + y):
                                routers_list[i][1] += 1
                                routers_list[i][3].add((X+x, Y+y))
                        except IndexError:
                            pass
                i+=1

    return routers_list



def dynamic_algorithm(routers_list):
    l = lambda x:(x[3],x[4],x[5])
    connecting_to_backbone_cost, router_cost,budget = l(reading_input_data("inputtext.txt"))
    dict_ = dict()
    sorted_routers_list = sorted(routers_list,key=lambda x:x[1]/x[2])
    dots_s = set()
    dots_list = []

    def recur(budget, i, dots_set):
        sorted_routers_listt = sorted([i for i in sorted_routers_list if i is not None], key=lambda x:len(x[3]-dots_set))
        dots = dots_set.copy()
        if budget in dict_:
            return dict_[budget]
        if i == 0 or budget == 0:
            dots_list.append(dots)
            return 0
        elif sorted_routers_listt[i][2] * connecting_to_backbone_cost + router_cost > budget:
            dict_[budget] = recur(budget, i -1, dots)
            return dict_[budget]
        else:
            d = dots.union(sorted_routers_listt[i][3])
            val = sorted_routers_listt[i][2] * connecting_to_backbone_cost + router_cost
            g = sorted_routers_listt[i][1] + recur(budget - val, i-1, d)
            gg = recur(budget, i - 1, dots)
            if g>gg:
                dict_[budget] = g
            else:
                dict_[budget] = gg
            return dict_[budget]
    asd = recur(budget, len(routers_list) - 1, dots_s)
    print(sorted(dots_list, key=lambda x:len(x))[-1])
    return asd

