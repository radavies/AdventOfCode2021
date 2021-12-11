from utils import read_input


class Eleventh:

    def __init__(self, debug):
        self.debug = debug
        self.octos = None
        self.everyone_flashed = False
        print("---- Eleventh Challenge ----")

    def one(self):
        self.octos = read_input(self.debug, 11, self.line_function)

        flash_counter = 0
        for step in range(1, 101):
            flash_counter += self.simulate()

        print("-- Part One --")
        print('Answer: {}\n'.format(flash_counter))

    def two(self):
        self.octos = read_input(self.debug, 11, self.line_function)

        step = 1
        while not self.everyone_flashed:
            self.simulate()
            if self.everyone_flashed:
                break
            step += 1

        print("-- Part Two --")
        print('Answer: {}\n'.format(step - 1))

    def simulate(self):
        all_zeros = True
        for y in range(0, len(self.octos)):
            for x in range(0, len(self.octos[0])):
                if self.octos[y][x] != 0:
                    all_zeros = False
                self.octos[y][x] += 1

        if all_zeros:
            self.everyone_flashed = True

        flash_counter = 0
        for y in range(0, len(self.octos)):
            for x in range(0, len(self.octos[0])):
                flash_counter += self.flash(x, y, False)

        return flash_counter

    def flash(self, x, y, from_flash):
        flash_counter = 0

        if self.octos[y][x] != 0:
            if from_flash:
                self.octos[y][x] += 1

            if self.octos[y][x] > 9:
                flash_counter += 1
                self.octos[y][x] = 0

                if y - 1 >= 0:
                    if x - 1 >= 0:
                        flash_counter += self.flash(x-1, y-1, True)
                    flash_counter += self.flash(x, y-1, True)
                    if x + 1 < len(self.octos[0]):
                        flash_counter += self.flash(x+1, y-1, True)

                if x - 1 >= 0:
                    flash_counter += self.flash(x-1, y, True)
                if x + 1 < len(self.octos[0]):
                    flash_counter += self.flash(x+1, y, True)

                if y + 1 < len(self.octos):
                    if x - 1 >= 0:
                        flash_counter += self.flash(x-1, y+1, True)
                    flash_counter += self.flash(x, y+1, True)
                    if x + 1 < len(self.octos[0]):
                        flash_counter += self.flash(x+1, y+1, True)

        return flash_counter

    @staticmethod
    def line_function(line):
        return list(map(int, line.strip()))
