from utils import read_input


class Sixteenth:

    def __init__(self, debug):
        self.debug = debug
        self.input = read_input(self.debug, 15, self.line_function)

        print("---- Sixteenth Challenge ----")

    def one(self):
        print("-- Part One --")
        print('Answer: {}\n'.format(0))

    def two(self):
        print("-- Part Two --")
        print('Answer: {}\n'.format(0))

    @staticmethod
    def line_function(line):
        return list(map(int, line.strip()))
