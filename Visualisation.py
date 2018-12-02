from ReadingData import reading_input_data, reading_output_data


def text_input_visualization(inputfilename):
    """
    :param inputfilename: Name of an input file
    :return: Text representation of input data
    """
    rows, cols, radius, connecting_to_backbone_cost, router_cost, budget, initial_backbone, cells_list = reading_input_data(inputfilename)
    print("""{0} rows, {1} columns, router range radius is {2}
backbone costs {3}, router costs {4}, budget is {5}
the initial cell connected to backbone is {6} """\
                            .format(rows, cols, radius, connecting_to_backbone_cost, router_cost, budget, initial_backbone))
    for i in cells_list:
        print("".join(i))

    return cells_list


def text_result_visualization(outputfilename, inputfilename):
    """
    :param outputfilename: Name of an input file
    :param inputfilename: Name of an output file
    :return: Text representation of already changed data
    """
    l = lambda x:(x[0],x[1])
    connected_cells_list, routers_list = l(reading_output_data(outputfilename))
    l = lambda x: (x[7],x[6])
    cells_list, initial_backbone = l(reading_input_data(inputfilename))

    for i in connected_cells_list:
        cells_list[i[0]][i[1]] = "c"
    for i in routers_list:
        cells_list[i[0]][i[1]] = "r"
    cells_list[initial_backbone[0]][initial_backbone[1]] = "b"

    for i in cells_list:
        print("".join(i))

    return cells_list


def text_connectedcells_visualization(outputfilename, inputfilename):
    """
    :param outputfilename: Name of an output file
    :param inputfilename: Name of an output file
    :return: Prints and returns the view of connected to network cells, which are denoted as "w"
    """

    def nowalls(cells_list, X, Y, x, y):
        for i in range(min(X, x), max(X, x) + 1):
            for j in range(min(X, y), max(Y, y) + 1):
                if cells_list[i][j] == "#":
                    return False
        return True
    placed = 0
    router_list = reading_output_data(outputfilename)[1]
    l = lambda x:(x[2],x[7])
    radius, cells_list = l(reading_input_data(inputfilename))

    print("Routers are placed in ",router_list, "positions")

    for m in router_list:
        X,Y = m[0],m[1]
        for x in range(-radius,radius+1):
            for y in range(-radius,radius+1):
                if nowalls(cells_list,X,Y,X+x,Y+y) and cells_list[X+x][Y+y] != "#" and cells_list[X+x][Y+y] == ".":
                    cells_list[X+x][Y+y] = "w"
                    placed += 1

    if __name__ == "__main__":  #Prints cells list if and only if it is called from this file
        for i in cells_list:
            print("".join(i))

    return cells_list, placed


if __name__ == "__main__":
    text_input_visualization("inputtext.txt")
    print("\n")
    text_result_visualization("outputtext.txt", "inputtext.txt")
    print("\n")
    text_connectedcells_visualization("outputtext.txt", "inputtext.txt")