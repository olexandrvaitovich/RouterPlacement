from AdditionalFunctions import nowalls
from ReadingData import reading_input_data

def greedy_algoritm(routers_list):
    l = lambda x: (x[3], x[4], x[5])
    connecting_to_backbone_cost, router_cost, budget = l(reading_input_data("inputtext.txt"))
    sorted_routers_list = sorted(routers_list, key=lambda x: x[1] / x[2])
    dots_s = set()
    n = 0
    i = len(sorted_routers_list)-1
    while n<budget and i!=0:
        sorted_routers_listt = sorted(sorted_routers_list, key=lambda x: len(x[3] - dots_s))
        if n+sorted_routers_listt[i][2] * connecting_to_backbone_cost + router_cost<budget:
            dots_s = dots_s.union(sorted_routers_listt[i][3])
            n+=sorted_routers_listt[i][2] * connecting_to_backbone_cost + router_cost
            k = len(dots_s)
        else:
            i-=1
    return dots_s