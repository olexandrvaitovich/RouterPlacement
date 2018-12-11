from AdditionalFunctions import nowalls
from AdditionalFunctions import finding_most_valid_routers2
from ReadingData import reading_input_data
from Scoring import count_points
import copy
def dynamic_algorithm(inputfile):
    l = lambda x:(x[3],x[4],x[5])
    connecting_to_backbone_cost, router_cost,budget = l(reading_input_data(inputfile))
    routers_list = finding_most_valid_routers2(inputfile)
    dict_ = dict()
    sorted_routers_list = sorted(routers_list,key=lambda x:x[1]/x[2])
    dots_s = set()
    dots_list = []

    def recur(budget, i, dots_set):
        sorted_routers_listt = sorted(sorted_routers_list, key=lambda x:len(x[3]-dots_set))
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
            d.add((sorted_routers_listt[i][0][0], sorted_routers_listt[i][0][1], "r"))
            val = sorted_routers_listt[i][2] * connecting_to_backbone_cost + router_cost
            g = sorted_routers_listt[i][1] + recur(budget - val, i-1, d)
            gg = recur(budget, i - 1, dots)
            if g>gg:
                dict_[budget] = g
            else:
                dict_[budget] = gg
            return dict_[budget]
    asd = recur(budget, len(routers_list) - 1, dots_s)
    d_set = list(max(dots_list))
    r_list = []
    for i in range(len(d_set)):
        if len(d_set[i]) == 3:
            r_list.append((d_set[i][0], d_set[i][1]))
    return len(d_set), d_set, len(r_list), r_list

