grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]


def num_islands_helper(grid, i, j):
    row = len(grid)
    col = len(grid[0])
    if i > row or j > col or i < 0 or j < 0 or grid[i][j] == '0' or grid[i][j] == '2':
        return

    grid[i][j] = '2'

    num_islands_helper(grid, i - 1, j)
    num_islands_helper(grid, i, j - 1)
    num_islands_helper(grid, i + 1, j)
    num_islands_helper(grid, i, j + 1)

def numIslands():
    row = len(grid)
    col = len(grid[0])
    count = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                count += 1
                num_islands_helper(grid, i, j)
    print(count)
numIslands()