from utils import read_input


class FoldingPuzzle:

    fold_along = []
    dot_map = []

    def __init__(self, debug):
        puzzle_input = read_input(debug, 13, self.line_function)

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

    @staticmethod
    def line_function(line):
        return line.strip()
