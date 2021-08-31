# https://www.hackerrank.com/challenges/cavity-map/problem
# !/bin/python3

def cavityMap(grid):
    grid = [list(x) for x in grid]

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            if grid[i][j] > grid[i + 1][j] and grid[i][j] > grid[i - 1][j] and grid[i][j] > grid[i][j + 1] and grid[i][j] > grid[i][j - 1]:
                grid[i][j] = 'X'

    return ["".join(x) for x in grid]


if __name__ == '__main__':
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(grid)
    print('\n'.join(result))
