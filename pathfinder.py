from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def find_path(start,end):
    initial_x, initial_y = start
    arrival_x, arrival_y = end
    
    matrix = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ]

    grid = Grid(matrix=matrix)

    start = grid.node(initial_x,initial_y)
    end = grid.node(arrival_x,arrival_y)

    finder = AStarFinder() 

    path, runs = finder.find_path(start, end, grid)

    path_coordinates = [(node.x, node.y) for node in path]

    print(path_coordinates)
    return path_coordinates

