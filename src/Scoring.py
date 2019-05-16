from src.ReadingData import reading_output_data, reading_input_data
from src.AdditionalFunctions import placing_connected_cells

def count_points(outputfilename,inputfilename):
    """
    :param outputfilename:The name of our resulted file
    :param inputfilename:The name of our input data file
    :return: Our algorithms score
    """
    l = lambda x:(x[2],x[3],x[4],x[5],x[7])
    radius, connecting_to_backbone_cost, router_cost, budget, cells_list = l(reading_input_data(inputfilename))
    l = lambda x:(x[1],x[2],x[3])
    routers_list, connected_cells, placed_routers = l(reading_output_data(outputfilename))
    placed = placing_connected_cells(routers_list, radius, cells_list)[1]

    return 1000*placed + (budget - (connected_cells * connecting_to_backbone_cost + placed_routers * router_cost))


if __name__ == "__main__":
    print(count_points("../txt/outputtext.txt","../txt/inputtext.txt"))
