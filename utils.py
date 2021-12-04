from pathlib import Path
from bingo import Bingo


def read_input(debug, challenge_number, line_func):
    folder = Path("inputs")

    if debug:
        file = folder / 'test{}.txt'.format(challenge_number)
    else:
        file = folder / "{}.txt".format(challenge_number)

    data = open(file)
    input_lines = []
    for line in data:
        input_lines.append(line_func(line))
    data.close()

    return input_lines


def read_bingo_input(debug):
    folder = Path("inputs")
    bingo = Bingo()

    if debug:
        file = folder / 'test{}.txt'.format(4)
    else:
        file = folder / "{}.txt".format(4)

    data = open(file)
    line_counter = 0
    current_board = []
    line_within_square_counter = 0
    for line in data:
        if line != '\n':
            if line_counter == 0:
                bingo.add_numbers_to_call(list(map(int, (str.split(line.strip(), ',')))))
            else:
                current_board.append(list(map(int, list(filter(bingo_filter_function, str.split(line.strip(), ' '))))))
                line_within_square_counter += 1
                if line_within_square_counter > 4:
                    bingo.add_board(current_board)
                    current_board = []
                    line_within_square_counter = 0

        line_counter += 1

    data.close()

    return bingo


def bingo_filter_function(to_filter):
    return to_filter != ''
