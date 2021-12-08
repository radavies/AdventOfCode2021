from utils import read_input
from seven_segment import SevenSegment


class Eighth:

    def __init__(self, debug):
        self.debug = debug
        self.input_output = read_input(self.debug, 8, self.line_function)
        print("---- Eighth Challenge ----")

    def one(self):
        total = 0
        for line in self.input_output:
            for output in line[1]:
                if len(output) == 7 or len(output) == 4 or len(output) == 3 or len(output) == 2:
                    total += 1

        print("-- Part One --")
        print('Answer: {}\n'.format(total))

    def two(self):
        total = 0
        for line in self.input_output:

            display = SevenSegment()

            for input in line[0]:
                if len(input) == 7:
                    display.add_to_map(8, input)
                elif len(input) == 4:
                    display.add_to_map(4, input)
                elif len(input) == 3:
                    display.add_to_map(7, input)
                elif len(input) == 2:
                    display.add_to_map(1, input)
                elif len(input) == 5:
                    display.add_to_two_three_or_five(input)
                elif len(input) == 6:
                    display.add_to_six_nine_or_zero(input)

            display.work_out_missing_numbers()
            total += display.get_answer_from_output(line[1])

        print("-- Part Two --")
        print('Answer: {}\n'.format(total))

    @staticmethod
    def line_function(line):
        initial_split = line.split('|')
        return [initial_split[0].strip().split(' '), initial_split[1].strip().split(' ')]
