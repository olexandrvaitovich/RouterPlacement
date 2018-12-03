def nowalls(cells_list, X, Y, x, y):
    for i in range(min(X, x), max(X, x) + 1):
        for j in range(min(Y, y), max(Y, y) + 1):
            if cells_list[i][j] == "#":
                return False
    return True