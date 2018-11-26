from ReadingData import reading_input_data, reading_output_data


def text_input_visualization(inputfilename):
    """
    :param inputfilename: Name of an input file
    :return: Text representation of input data
    """
    rows, cols, radius, backbone_cost, router_cost, budget, initial_backbone, cells_list = reading_input_data(inputfilename)
    print("""{0} rows, {1} columns, router range radius is {2}
backbone costs {3}, router costs {4}, budget is {5}
the initial cell connected to backbone is {6} """\
                            .format(rows, cols, radius, backbone_cost, router_cost, budget, initial_backbone))
    for i in cells_list:
        print("".join(i))

    return cells_list


def text_result_visualization(outputfilename, inputfilename):
    """
    :param outputfilename: Name of an input file
    :param inputfilename: Name of an output file
    :return: Text representation of already changed data
    """
    connected_cells_list, routers_list = reading_output_data(outputfilename)
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


def graph_input_visualization(filename):
    pass

if __name__ == "__main__":
    pass