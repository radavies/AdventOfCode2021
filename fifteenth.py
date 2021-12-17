import math

from utils import read_input
from path_node import PathNode
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.dijkstra import DijkstraFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

class Fifteenth:

    def __init__(self, debug):
        self.debug = debug
        self.map = read_input(self.debug, 15, self.line_function)
        self.total_path_score = 0
        print("---- Fifteenth Challenge ----")

    def one(self):
        path_taken = self.find_least_risky_path()
        answer = self.get_path_score(path_taken)
        print("-- Part One --")
        print('Answer: {}\n'.format(answer))

    def two_using_a_lib(self):
        mega_map = self.build_mega_map()
        mega_map_copy = self.build_mega_map()
        self.map = mega_map
        grid = Grid(matrix=mega_map_copy)
        start = grid.node(0, 0)
        end = grid.node(len(self.map[0]) - 1, len(self.map) - 1)
        finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)

        print('operations:', runs, 'path length:', len(path))
        # print(grid.grid_str(path=path, start=start, end=end))

        answer = self.get_path_score(path)
        print("-- Part Two (using a lib) --")
        print('Answer: {}\n'.format(answer - 1))

    def two(self):
        mega_map = self.build_mega_map()
        self.map = mega_map
        path_taken = self.find_least_risky_path()
        answer = self.get_path_score(path_taken)
        print("-- Part Two --")
        print('Answer: {}\n'.format(answer))

    def build_mega_map(self):
        mega_map = []
        y_counter = 0
        x_counter = 0

        for mega_y_counter in range(0, len(self.map) * 5):
            new_line = []
            for mega_x_counter in range(0, len(self.map[0]) * 5):
                path_score_additions = math.floor(mega_x_counter / 10) + math.floor(mega_y_counter / 10)
                new_item = self.map[y_counter][x_counter] + path_score_additions
                if new_item > 9:
                    new_item = new_item - 9
                new_line.append(new_item)

                x_counter += 1
                if x_counter >= len(self.map[0]):
                    x_counter = 0

            mega_map.append(new_line)

            y_counter += 1
            if y_counter >= len(self.map):
                y_counter = 0

        return mega_map

    def find_least_risky_path(self):
        open_list = []
        closed_list = []
        start_node = PathNode(0, [0, 0], None)

        open_list.append(start_node)

        end_node = PathNode(self.map[len(self.map) - 1][len(self.map[0]) - 1], [len(self.map[0]) - 1, len(self.map) - 1], None)

        while len(open_list) > 0:
            open_list.sort()
            current_node = open_list.pop(0)
            closed_list.append(current_node)

            if current_node == end_node:
                path_taken = []
                while current_node != start_node:
                    path_taken.append(current_node.coords)
                    current_node = current_node.parent
                return path_taken[::-1]

            (x, y) = current_node.coords
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

            for neighbor in neighbors:
                (neighbor_x, neighbor_y) = neighbor
                if neighbor_x >= 0 and neighbor_y >= 0 and (neighbor_x <= len(self.map[0]) - 1) and (neighbor_y <= len(self.map) - 1):
                    neighbor_node = PathNode(self.map[neighbor_y][neighbor_x], [neighbor_x, neighbor_y], current_node)
                    if neighbor_node not in closed_list:

                        neighbor_node.total_cost = neighbor_node.my_cost + neighbor_node.parent.total_cost

                        if neighbor_node in open_list:
                            existing = open_list[open_list.index(neighbor_node)]
                            if existing.total_cost > neighbor_node.total_cost:
                                existing.parent = current_node
                                existing.total_cost = neighbor_node.total_cost
                        else:
                            open_list.append(neighbor_node)

        return None

    @staticmethod
    def add_to_open(open_list, new_node):
        for node in open_list:
            if new_node == node and new_node.f >= node.f:
                return False
        return True

    def get_path_score(self, path_taken):
        score = 0
        for point in path_taken:
            score += self.map[point[1]][point[0]]
        return score

    def print_path(self, path_taken):
        print_map = [row[:] for row in self.map]

        for point in path_taken:
            print_map[point[1]][point[0]] = "X"

        for line in print_map:
            print(self.format_line_to_print(line))
        print()

    @staticmethod
    def format_line_to_print(line):
        output = ""
        for item in line:
            output += str(item)
        return output

    @staticmethod
    def line_function(line):
        return list(map(int, line.strip()))
