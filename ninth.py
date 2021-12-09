from utils import read_input


class Ninth:

    def __init__(self, debug):
        self.debug = debug
        self.map = read_input(self.debug, 9, self.line_function)
        print("---- Ninth Challenge ----")

    def one(self):
        low_points = self.find_low_points()
        answer = self.calculate_danger_score(low_points)
        print("-- Part One --")
        print('Answer: {}\n'.format(answer))

    def two(self):
        low_points = self.find_low_points()
        answer = self.find_top_three_basin_score(low_points)
        print("-- Part Two --")
        print('Answer: {}\n'.format(answer))

    def find_low_points(self):
        low_points = []
        for x in range(0, len(self.map[0])):
            for y in range(0, len(self.map)):
                if self.check_is_lowest(x, y):
                    low_points.append([x, y])
        return low_points

    def check_is_lowest(self, x, y):
        return self.check_x_lowest(x, y) and self.check_y_lowest(x, y)

    def check_x_lowest(self, x, y):
        current = self.map[y][x]
        is_low = True
        if x - 1 >= 0:
            if current >= self.map[y][x-1]:
                is_low = False
        if x + 1 < len(self.map[y]):
            if current >= self.map[y][x + 1]:
                is_low = False
        return is_low

    def check_y_lowest(self, x, y):
        current = self.map[y][x]
        is_low = True
        if y - 1 >= 0:
            if current >= self.map[y - 1][x]:
                is_low = False
        if y + 1 < len(self.map):
            if current >= self.map[y + 1][x]:
                is_low = False
        return is_low

    def calculate_danger_score(self, low_points):
        total = 0
        for low_point in low_points:
            total += (1 + self.map[low_point[1]][low_point[0]])
        return total

    def find_top_three_basin_score(self, low_points):
        basins = []
        for low_point in low_points:
            basins.append(self.find_basin_score_from_low_point(low_point))

        basins.sort(reverse=True)
        answer = basins[0] * basins[1] * basins[2]
        return answer

    def find_basin_score_from_low_point(self, low_point):
        points_in_basin = []
        points_to_check = [low_point]

        while len(points_to_check) > 0:
            new_points = []
            for point in points_to_check:
                points_in_basin.append(point)
                new_x_points = self.check_x_in_basin(point[0], point[1])
                new_y_points = self.check_y_in_basin(point[0], point[1])
                if len(new_x_points) > 0:
                    for new_point in new_x_points:
                        if new_point not in points_in_basin and new_point not in new_points \
                                and new_point not in points_to_check:
                            new_points.append(new_point)
                if len(new_y_points) > 0:
                    for new_point in new_y_points:
                        if new_point not in points_in_basin and new_point not in new_points \
                                and new_point not in points_to_check:
                            new_points.append(new_point)

            points_to_check = new_points

        return len(points_in_basin)

    def check_x_in_basin(self, x, y):
        current = self.map[y][x]
        points_in_basin = []
        if x - 1 >= 0:
            if current <= self.map[y][x - 1] != 9:
                points_in_basin.append([x - 1, y])
        if x + 1 < len(self.map[y]):
            if current <= self.map[y][x + 1] != 9:
                points_in_basin.append([x + 1, y])
        return points_in_basin

    def check_y_in_basin(self, x, y):
        current = self.map[y][x]
        points_in_basin = []
        if y - 1 >= 0:
            if current <= self.map[y - 1][x] != 9:
                points_in_basin.append([x, y - 1])
        if y + 1 < len(self.map):
            if current <= self.map[y + 1][x] != 9:
                points_in_basin.append([x, y + 1])
        return points_in_basin

    @staticmethod
    def line_function(line):
        return list(map(int, line.strip()))
