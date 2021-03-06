import statistics

from utils import read_input


class Seventh:

    def __init__(self, debug):
        self.debug = debug
        self.subs = read_input(self.debug, 7, self.line_function)[0]
        self.subs.sort()
        print("---- Seventh Challenge ----")

    def one(self):
        place_to_move_to = int(statistics.median(self.subs))

        total_fuel_spent = 0
        for sub in self.subs:
            total_fuel_spent += abs(sub - place_to_move_to)

        print("-- Part One --")
        print('Answer: {}\n'.format(total_fuel_spent))

    def two(self):
        final_fuel_spend = -1
        complete_sequence = self.get_complete_sequence()

        for place_to_move_to in complete_sequence:
            total_fuel_spent = 0
            for sub in self.subs:
                places_moved = abs(sub - place_to_move_to)
                fuel_spent = 0
                for x in range(1, places_moved + 1):
                    fuel_spent += (1 * x)
                total_fuel_spent += fuel_spent
            if total_fuel_spent < final_fuel_spend or final_fuel_spend == -1:
                final_fuel_spend = total_fuel_spent

        print("-- Part Two --")
        print('Answer: {}\n'.format(final_fuel_spend))

    def better_two(self):

        starting_point = int(statistics.mean(self.subs))
        final_fuel_spend = self.get_fuel_score(starting_point)
        found_lowest = False

        counter = 1
        while not found_lowest:
            low_score = self.get_fuel_score(starting_point - counter)
            high_score = self.get_fuel_score(starting_point + counter)

            if low_score < final_fuel_spend or high_score < final_fuel_spend:
                final_fuel_spend = low_score if low_score < high_score else high_score
                counter += 1
            else:
                found_lowest = True

        print("-- Part Two (better) --")
        print('Answer: {}\n'.format(final_fuel_spend))

    def get_fuel_score(self, place_to_move_to):
        total_fuel_spent = 0
        for sub in self.subs:
            places_moved = abs(sub - place_to_move_to)
            fuel_spent = 0
            for x in range(1, places_moved + 1):
                fuel_spent += (1 * x)
            total_fuel_spent += fuel_spent

        return total_fuel_spent

    def get_complete_sequence(self):
        sequence = list(dict.fromkeys(self.subs))
        numbers_to_add = []
        previous_number = 0
        for number in sequence:
            difference = number - previous_number
            if difference > 1:
                for counter in range(1, difference):
                    numbers_to_add.append(previous_number + counter)
            previous_number = number

        sequence.extend(numbers_to_add)
        sequence.sort()
        return sequence

    @staticmethod
    def line_function(line):
        return list(map(int, line.split(',')))
