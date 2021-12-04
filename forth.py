from utils import read_bingo_input


class Forth:

    debug = False
    bingo = None

    def __init__(self, debug):
        self.debug = debug

        print("---- Forth Challenge ----")

    def one(self):
        self.bingo = read_bingo_input(self.debug)

        winner = None
        last_number_drawn = None
        while winner is None:
            last_number_drawn = self.bingo.mark_boards()
            winners = self.bingo.check_for_winners()
            if len(winners) > 0:
                winner = winners.pop(0)

        answer = self.bingo.calculate_winning_score(winner, last_number_drawn)

        print("-- Part One --")
        print('Answer: {}\n'.format(answer))

    def two(self):
        self.bingo = read_bingo_input(self.debug)

        list_of_winners_and_numbers = []
        list_of_winners = []
        while self.bingo.get_count_of_numbers_left_to_call() > 0 and len(list_of_winners) < len(self.bingo.boards):
            last_number_drawn = self.bingo.mark_boards_ignore_winners(list_of_winners)
            next_winners = self.bingo.check_for_winners_ignore_previous(list_of_winners)
            if len(next_winners) > 0:
                for winner in next_winners:
                    list_of_winners.append(winner)
                    list_of_winners_and_numbers.append([winner, last_number_drawn])

        winner_pair = list_of_winners_and_numbers.pop()
        answer = self.bingo.calculate_winning_score(winner_pair[0], winner_pair[1])

        print("-- Part Two --")
        print('Answer: {}\n'.format(answer))


