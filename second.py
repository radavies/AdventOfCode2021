from utils import read_input


class Second:

    debug = False
    instructions = None

    def __init__(self, debug):
        self.debug = debug
        self.instructions = self.get_instructions()
        print("---- Second Challenge ----")

    def one(self):

        horizontal_pos = 0
        depth = 0

        for instruction in self.instructions:
            if instruction[0] == "forward":
                horizontal_pos += instruction[1]
            else:
                if instruction[0] == "up":
                    depth -= instruction[1]
                else:
                    depth += instruction[1]

        print("-- Part One --")
        print('Answer: {}\n'.format(horizontal_pos * depth))

    def two(self):
        horizontal_pos = 0
        depth = 0
        aim = 0

        for instruction in self.instructions:
            if instruction[0] == "forward":
                horizontal_pos += instruction[1]
                depth += (aim * instruction[1])
            else:
                if instruction[0] == "up":
                    aim -= instruction[1]
                else:
                    aim += instruction[1]

        print("-- Part Two --")
        print('Answer: {}\n'.format(horizontal_pos * depth))

    def get_instructions(self):
        return read_input(self.debug, 2, self.line_function)

    @staticmethod
    def line_function(line):
        split = str.split(line, " ")
        return [split[0], int(split[1])]
