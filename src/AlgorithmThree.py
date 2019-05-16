from src.AdditionalFunctions import finding_most_valid_routers2
from src.ReadingData import reading_input_data

def greedy_algorithm(inputfile):
    l = lambda x: (x[3], x[4], x[5])
    connecting_to_backbone_cost, router_cost, budget = l(reading_input_data(inputfile))
    routers_list = finding_most_valid_routers2(inputfile)
    print(1)
    sorted_routers_list = sorted(routers_list, key=lambda x: x[1] / x[2])
    dots_s = set()
    n = 0
    i = len(sorted_routers_list)-1
    sorted_routers_listt = sorted_routers_list[:]
    while n<budget and i!=0:
        if n+sorted_routers_listt[i][2] * connecting_to_backbone_cost + router_cost<budget:
            sorted_routers_listt = sorted(sorted_routers_list, key=lambda x: len(x[3] - dots_s))
            dots_s = dots_s.union(sorted_routers_listt[i][3])
            dots_s.add((sorted_routers_listt[i][0][0], sorted_routers_listt[i][0][1], "r"))
            n+=sorted_routers_listt[i][2] * connecting_to_backbone_cost + router_cost
        else:
            i-=1
    r_list = []
    dots_s = list(dots_s)
    for i in range(len(dots_s)):
        if len(dots_s[i]) == 3:
            r_list.append((dots_s[i][0], dots_s[i][1]))
    return len(dots_s), dots_s, len(r_list), r_list