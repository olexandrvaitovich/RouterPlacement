from ReadingData import reading_input_data, reading_output_data


def text_input_visualization(inputfilename):
    rows, cols, radius, backbone_cost, router_cost, budget, connected_cell, cells_list = reading_input_data(inputfilename)
    print("""{0} rows, {1} columns, router range radius is {2}
backbone costs {3}, router costs {4}, budget is {5}
the initial cell connected to backbone is {6} """\
                            .format(rows, cols, radius, backbone_cost, router_cost, budget, connected_cell))
    for i in cells_list:
        print(i)

def text_result_visualization(outputfilename):
    connected_cells_list, routers_list = reading_output_data(outputfilename)

def graph_input_visualization(filename):
    pass

if __name__ == "__main__":
    result_visualization("outputtext.txt")