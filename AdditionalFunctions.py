from ReadingData import reading_input_data


def nowalls(cells_list, X, Y, x, y):
    """
    Function that check whether there is a walls acording to a task description
    """
    for i in range(min(X, x), max(X, x) + 1):
        for j in range(min(Y, y), max(Y, y) + 1):
            if cells_list[i][j] == "#":
                return False
    return True


def placing_connected_cells(router_list, radius, cells_list):
    """
    Function that marks covered spots with letter "w"
    """
    placed = 0

    for m in router_list:
        X, Y = m[0], m[1]
        try:
            for x in range(-radius, radius + 1):
                for y in range(-radius, radius + 1):
                    if nowalls(cells_list, X, Y, X + x, Y + y) and cells_list[X + x][Y + y] != "#" and \
                            cells_list[X + x][Y + y] == ".":
                        cells_list[X + x][Y + y] = "w"
                        placed += 1
        except:
            pass

    return cells_list, placed


def calc_dist(backbone, router):
    return max(abs(backbone[0] - router[0]), abs(backbone[1] - router[1]))


def find_connected_tobackbone_cells(backbone, router):
    list_ = list()
    if backbone[0] == router[0]:
        return [[backbone[0],i] for i in range(min(backbone[1],router[1]), max(backbone[1],router[1]))]
    elif backbone[1] == router[1]:
        return [[i, backbone[1]] for i in range(min(backbone[0],router[0]), max(backbone[0],router[0]))]
    else:
        while backbone[0] > router[0]:
            list_.append((router[0],router[1]))
            router[0] += 1
            router[1] += 1
        while backbone[0] < router[0]:
            list_.append((backbone[0],backbone[1]))
            backbone[0] += 1
            backbone[1] += 1
        while backbone[1] > router[1]:
            list_.append((router[0],router[1]))
            router[1] += 1
        while backbone[1] < router[1]:
            list_.append((backbone[0],backbone[1]))
            backbone[1] += 1

    return list_



def finding_most_valid_routers(inputfilename):
    """
    :param inputfilename: The name of our input data file
    :return: List of possible placed routers with coordinates as a first param, coverage as second and distance to
    backbone as third
    """

    rows, cols, radius, connecting_to_backbone_cost, router_cost, budget,\
                                            initial_backbone, cells_list = reading_input_data(inputfilename)

    routers_list = list()
    i = 0

    for X in range(rows):
        for Y in range(cols):
            distance = calc_dist(initial_backbone, (X,Y))
            if distance != 0 and cells_list[X][Y] == ".":  #Adding routers that are not backbone pos and in . pos
                #connected_cells = find_connected_tobackbone_cells(list(initial_backbone), [X,Y])
                routers_list.append([(X,Y),0,distance,None])#connected_cells])
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
def finding_most_valid_routers2(inputfilename):
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
