from utils import read_input

class FoldingPuzzle:

    def __init__(self, debug):
        puzzle_input = read_input(debug, 13, self.line_function)

        self.fold_along = []
        self.dot_map = []

        max_x = 0
        max_y = 0
        dots = []
        for line in puzzle_input:
            if len(line) > 0:
                if line.startswith("fold along"):
                    bits = line.split(' ')[2].split('=')
                    self.fold_along.append([bits[0], int(bits[1])])
                else:
                    coords = list(map(int, line.split(',')))
                    if coords[0] > max_x:
                        max_x = coords[0]
                    if coords[1] > max_y:
                        max_y = coords[1]

                    dots.append(coords)

        self.dot_map = [[''] * (max_x + 1) for y in range(max_y + 1)]

        for dot in dots:
            self.dot_map[dot[1]][dot[0]] = '#'

    def fold_to_end(self):
        fold_number = 1
        while len(self.fold_along) > 0:
            self.fold(True)
            self.print_map(fold_number)
            fold_number += 1

    def count_dots(self):
        dot_count = 0
        for line in self.dot_map:
            for item in line:
                if item == '#':
                    dot_count += 1
        return dot_count

    def print_map(self, fold_number):
        if fold_number is not None:
            print('- Fold: {} -'.format(fold_number))
        for line in self.dot_map:
            print(self.format_line_to_print(line))
        print()

    @staticmethod
    def format_line_to_print(line):
        output = ""
        for item in line:
            if item == '':
                output += '.'
            else:
                output += item
        return output

    def fold(self, print_fold_maps):
        fold_command = self.fold_along.pop(0)

        if fold_command[0] == 'x':
            for y in range(0, len(self.dot_map)):
                self.dot_map[y][fold_command[1]] = '-'
            self.do_x_fold_translation(print_fold_maps, fold_command[1])
        else:
            for x in range(0, len(self.dot_map[fold_command[1]])):
                self.dot_map[fold_command[1]][x] = '-'
            self.do_y_fold_translation(print_fold_maps, fold_command[1])

    def do_y_fold_translation(self, print_fold_maps, fold_at):
        translated_y = 0

        new_map = self.create_new_dot_map_for_y_fold(fold_at)

        if print_fold_maps:
            self.print_map(None)

        for y in reversed(range(fold_at, len(self.dot_map))):
            for x in range(0, len(self.dot_map[0])):
                if self.dot_map[y][x] == '#' and new_map[translated_y][x] != '#':
                    new_map[translated_y][x] = '#'
            translated_y += 1
        self.dot_map = new_map

    def do_x_fold_translation(self, print_fold_maps, fold_at):
        new_map = self.create_new_dot_map_for_x_fold(fold_at)

        if print_fold_maps:
            self.print_map(None)

        for y in range(0, len(self.dot_map)):
            translated_x = 0
            for x in reversed(range(fold_at, len(self.dot_map[0]))):
                if self.dot_map[y][x] == '#' and new_map[y][translated_x] != '#':
                    new_map[y][translated_x] = '#'
                translated_x += 1
        self.dot_map = new_map

    def create_new_dot_map_for_y_fold(self, fold_at):
        new_map = []
        for y in range(0, fold_at):
            new_line = []
            for x in range(0, len(self.dot_map[0])):
                new_line.append(self.dot_map[y][x])
            new_map.append(new_line)
        return new_map

    def create_new_dot_map_for_x_fold(self, fold_at):
        new_map = []
        for y in range(0, len(self.dot_map)):
            new_line = []
            for x in range(0, fold_at):
                new_line.append(self.dot_map[y][x])
            new_map.append(new_line)
        return new_map

    @staticmethod
    def line_function(line):
        return line.strip()
