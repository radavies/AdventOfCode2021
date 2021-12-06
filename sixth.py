from utils import read_input


class Sixth:

    def __init__(self, debug):
        self.debug = debug
        self.fish = None
        print("---- Sixth Challenge ----")

    def one(self):
        self.fish = read_input(self.debug, 6, self.line_function)[0]
        for counter in range(0, 80):
            fish_counter = 0
            to_add = []
            for fishy in self.fish:
                if fishy == 0:
                    self.fish[fish_counter] = 6
                    to_add.append(8)
                else:
                    self.fish[fish_counter] = self.fish[fish_counter] - 1

                fish_counter += 1
            self.fish.extend(to_add)

        print("-- Part One --")
        print('Answer: {}\n'.format(len(self.fish)))

    def two(self):

        fish_states = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0
        }

        for fishy in read_input(self.debug, 6, self.line_function)[0]:
            fish_states[fishy] += 1

        for counter in range(0, 256):
            new_states = {
                0: 0,
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0,
                8: 0
            }
            for state in reversed(range(0, 9)):
                if state != 0:
                    new_states[state - 1] = fish_states[state]
                else:
                    new_states[8] = fish_states[0]
                    new_states[6] = new_states[6] + fish_states[0]

            fish_states = new_states

        total_fish = 0
        for state in range(0, 9):
            total_fish += fish_states[state]

        print("-- Part Two --")
        print('Answer: {}\n'.format(total_fish))

    @staticmethod
    def line_function(line):
        return list(map(int, line.split(',')))
