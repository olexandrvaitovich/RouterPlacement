def reading_input_data(inputfilename):
    """
    :param inputfilename: The name of our input data file
    :return: All the data needed for the calculation
    """
    with open(inputfilename) as file:
        data = file.readlines()
    rows, cols, radius = map(int,data[0].split(" "))
    connecting_to_backbone_cost, router_cost, budget = map(int,data[1].split(" "))
    initial_backbone = tuple(map(int,data[2].strip().split(" ")))
    cells_list = [list(data[i].strip()) for i in range(3,3+rows)]

    return rows, cols, radius, connecting_to_backbone_cost, router_cost, budget, initial_backbone, cells_list

def reading_output_data(outputfilename):
    """
    :param outputfilename: The name of our resulted file
    :return: List of cells that were connected to a backbone by our algorithm and a list of placed routers.
    """
    connected_cells_list, routers_list = list(), list()
    with open(outputfilename) as file:
        connected_cells = int(file.readline())
        for i in range(connected_cells):
            connected_cells_list.append(tuple(map(int, file.readline().strip().split(" "))))
        placed_routers = int(file.readline())
        for i in range(placed_routers):
            routers_list.append(tuple(map(int, file.readline().replace("(","").replace(")","").replace(",","").strip().split(" "))))

    return connected_cells_list, routers_list, connected_cells, placed_routers