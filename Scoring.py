from ReadingData import reading_output_data, reading_input_data
from Visualisation import text_connectedcells_visualization

def count_points(outputfilename,inputfilename):
    """
    :param outputfilename:The name of our resulted file
    :param inputfilename:The name of our input data file
    :return: Our algorithms score
    """
    cells_list, placed = text_connectedcells_visualization(outputfilename, inputfilename)
    l = lambda x:(x[3],x[4],x[5])
    connecting_to_backbone_cost, router_cost, budget = l(reading_input_data(inputfilename))
    l = lambda x:(x[2],x[3])
    connected_cells, placed_routers = l(reading_output_data(outputfilename))

    return 1000*placed + (budget - (connected_cells * connecting_to_backbone_cost + placed_routers * router_cost))


if __name__ == "__main__":
    print(count_points("outputtext.txt","inputtext.txt"))
