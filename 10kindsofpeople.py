
"""
The solution is to fill (color/flood) each region from "start". If start and end has the
same color (or altitude or whatever) after filling the region, there exists
a path from start to end. Each region of ones is filled with a unique even number
and each region of zeroes with a unique odd number. Then, if start and end are the same
even number, "decimal" may travel from start to end, and if odd - "binary", else "neither".

A region will be filled only if the start position is 1 or 0. This results in an efficient
O(N) solution, where N is the number of cells in the grid.
"""

def fill(grid, start, clr):
    stack  = []
    kind = grid[start[0]][start[1]]
    stack.append(start)

    while len(stack) > 0:
        current = stack.pop()
        if grid[current[0]][current[1]] != clr:
            add_adjacent(grid, current, kind, stack)
            grid[current[0]][current[1]] = clr


def exists_path(grid, start, end):
    return grid[start[0]][start[1]] == grid[end[0]][end[1]]


def vector_add(u, v):
    return u[0] + v[0], u[1] + v[1]


def add_adjacent(grid, node, kind, stack):
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    for dv in d:
        adj = vector_add(node, dv)
        if in_bounds(grid, adj):
            if grid[adj[0]][adj[1]] == kind:
                stack.append(adj)


def in_bounds(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


def kind_mapping(node, k):
    return 2*k if node % 2 == 0 else 2*k + 1


def main():
    grid = []
    row_columns = list(map(lambda x: int(x), input().split()))
    for r in range(row_columns[0]):
        grid.append(list(map(lambda x: int(x), list(input()))))
    clr = 3
    for test in range(int(input())):
        pos = list(map(lambda x: int(x) - 1, input().split()))
        start = (pos[0], pos[1])
        end   = (pos[2], pos[3])
        kind = grid[start[0]][start[1]]
        if kind <= 1:
            fill(grid, start, kind_mapping(kind, clr))
            clr += 1

        print("neither" if not exists_path(grid, start, end) else "decimal" if kind % 2 == 1 else "binary")



if __name__ == '__main__':
    main()

