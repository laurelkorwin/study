def validate_board(lst):

    # creates the valid range of numbers you are looking for in each row, column and subgrid
    valid_nums = set(range(1, len(lst) + 1))

    # first, goes through each list in the input list (aka, each row) to make sure each is valid
    for row in lst:
        if set(row) != valid_nums:
            return False

    # constructs lists for each "column" in the input, and checks each column against the valid set
    for i in range(len(lst)):
        column = [row[i] for row in lst]
        if set(column) != valid_nums:
            return False

    # go through the grid again and construct subgrids of 3 (based on i and j indexes of 0, 3, and 6)
    # check if each subgrid is valid
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            grid = set()
            for x in range(3):
                for y in range(3):
                    grid.add(lst[i + x][j + y])
            if grid != valid_nums:
                return False

    return True
