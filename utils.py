from pathlib import Path


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
