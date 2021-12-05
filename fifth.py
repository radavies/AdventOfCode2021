from utils import read_input


class Fifth:

    debug = False
    co_ords = []
    gird = []

    def __init__(self, debug):
        self.debug = debug
        self.co_ords = read_input(self.debug, 5, self.line_function)

        print("---- Fifth Challenge ----")

    def one(self):
        self.init_answer_grid()

        for line in self.co_ords:
            if line[0][0] == line[1][0]:
                self.increment_vert_line(line[0][1], line[1][1], line[0][0])
            elif line[0][1] == line[1][1]:
                self.increment_hor_line(line[0][0], line[1][0], line[0][1])

        answer = self.count_danger_spaces()

        print("-- Part One --")
        print('Answer: {}\n'.format(answer))

    def two(self):
        self.init_answer_grid()

        for line in self.co_ords:
            if line[0][0] == line[1][0]:
                self.increment_vert_line(line[0][1], line[1][1], line[0][0])
            elif line[0][1] == line[1][1]:
                self.increment_hor_line(line[0][0], line[1][0], line[0][1])
            else:
                self.increment_diag_line(line[0][0], line[1][0], line[0][1], line[1][1])

        answer = self.count_danger_spaces()

        print("-- Part Two --")
        print('Answer: {}\n'.format(answer))

    def increment_hor_line(self, x_one, x_two, y):
        if x_one < x_two:
            x_start = x_one
            x_end = x_two
        else:
            x_start = x_two
            x_end = x_one

        for x in range(x_start, x_end + 1):
            self.gird[y][x] += 1

    def increment_vert_line(self, y_one, y_two, x):
        if y_one < y_two:
            y_start = y_one
            y_end = y_two
        else:
            y_start = y_two
            y_end = y_one

        for y in range(y_start, y_end + 1):
            self.gird[y][x] += 1

    def increment_diag_line(self, x_one, x_two, y_one, y_two):
        if y_one < y_two:
            y_start = y_one
            x_start = x_one

            y_end = y_two
            x_end = x_two
        else:
            y_start = y_two
            x_start = x_two

            y_end = y_one
            x_end = x_one

        if x_start < x_end:
            x = x_start
            for y in range(y_start, y_end + 1):
                self.gird[y][x] += 1
                x += 1
                if x > x_end:
                    break
        else:
            x = x_start
            for y in range(y_start, y_end + 1):
                self.gird[y][x] += 1
                x -= 1
                if x < 0:
                    break

    def init_answer_grid(self):
        largest_x = 0
        largest_y = 0

        for line in self.co_ords:
            for xy in line:
                if xy[0] > largest_x:
                    largest_x = xy[0]
                if xy[1] > largest_y:
                    largest_y = xy[1]

        self.gird = [[0] * (largest_x + 1) for y in range(largest_y + 1)]

    def count_danger_spaces(self):
        danger_count = 0

        for line in self.gird:
            for cell in line:
                if cell >= 2:
                    danger_count += 1

        return danger_count

    @staticmethod
    def line_function(line):
        start_end_split = str.split(line.strip(),  " -> ")
        coord_pair = [list(map(int, start_end_split[0].split(','))), list(map(int, start_end_split[1].split(',')))]
        return coord_pair
