from utils import read_input


class Fourteenth:

    def __init__(self, debug):
        self.debug = debug
        self.pairs = {}
        self.input = []
        self.sequence = []
        self.inserts = {}
        print("---- Fourteenth Challenge ----")

    def one(self):
        self.do_set_up()
        self.set_up_initial_pairs()

        for x in range(1, 11):
            self.do_steps()

        answer = self.calc_answer()

        print("-- Part One --")
        print('Answer: {}\n'.format(answer))

    def two(self):
        self.do_set_up()
        self.set_up_initial_pairs()

        for x in range(1, 41):
            self.do_steps()

        answer = self.calc_answer()

        print("-- Part Two --")
        print('Answer: {} (this might be out by one)\n'.format(answer))

    def do_steps(self):
        changes = {}
        for insert in self.inserts.items():
            if insert[0] in self.pairs and self.pairs[insert[0]] > 0:
                self.update_changes(changes, insert[0], -1 * self.pairs[insert[0]])
                new_pair_one = insert[0][0] + insert[1]
                new_pair_two = insert[1] + insert[0][1]
                self.update_changes(changes, new_pair_one, 1 * self.pairs[insert[0]])
                self.update_changes(changes, new_pair_two, 1 * self.pairs[insert[0]])

        self.do_updates_to_pairs(changes)

    def calc_answer(self):
        length = 0
        element_counts = {}
        for pair in self.pairs.items():
            length += 1 * pair[1]
            if pair[1] > 0:
                for element in pair[0]:
                    if element in element_counts:
                        element_counts[element] += 1 * pair[1]
                    else:
                        element_counts[element] = 1 * pair[1]

        most = -1
        least = -1
        for score in element_counts.items():
            if score[1] > most:
                most = score[1]
            if least == -1 or score[1] < least:
                least = score[1]

        return round((most / 2) - (least / 2))

    def do_updates_to_pairs(self, changes):
        for change in changes.items():
            if change[0] in self.pairs:
                self.pairs[change[0]] += change[1]
                if self.pairs[change[0]] < 0:
                    self.pairs[change[0]] = 0
            else:
                if change[1] > 0:
                    self.pairs[change[0]] = change[1]

    @staticmethod
    def update_changes(changes, key, change):
        if key in changes:
            changes[key] += change
        else:
            changes[key] = change

    def set_up_initial_pairs(self):
        self.pairs = {}
        element_counter = 1
        for element in self.sequence:
            pair = element + self.sequence[element_counter]
            if pair in self.pairs:
                self.pairs[pair] += 1
            else:
                self.pairs[pair] = 1

            element_counter += 1
            if element_counter >= len(self.sequence):
                break

    def set_up_inserts_dict(self):
        inserts_dict = {}
        for insert in self.input:
            inserts_dict[insert[0]] = insert[1]
        return inserts_dict

    def do_set_up(self):
        self.input = read_input(self.debug, 14, self.line_function)
        self.sequence = self.input.pop(0)
        self.input.pop(0)
        self.inserts = self.set_up_inserts_dict()

    @staticmethod
    def line_function(line):

        if '>' not in line:
            return list(line.strip())

        return list(map(str.strip, line.split('->')))


