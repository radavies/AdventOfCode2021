from first import First
from second import Second


def start(debug):
    first(debug)
    second(debug)

def first(debug):
    challenge = First(debug)
    challenge.one()
    challenge.two()


def second(debug):
    challenge = Second(debug)
    challenge.one()
    challenge.two()


if __name__ == '__main__':
    start(False)
