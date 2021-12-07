from first import First
from second import Second
from third import Third
from forth import Forth
from fifth import Fifth
from sixth import Sixth
from seventh import Seventh


def start(debug):
    first(debug)
    second(debug)
    third(debug)
    forth(debug)
    fifth(debug)
    sixth(debug)
    seventh(debug)


def first(debug):
    challenge = First(debug)
    challenge.one()
    challenge.two()


def second(debug):
    challenge = Second(debug)
    challenge.one()
    challenge.two()


def third(debug):
    challenge = Third(debug)
    challenge.one()
    challenge.two()


def forth(debug):
    challenge = Forth(debug)
    challenge.one()
    challenge.two()


def fifth(debug):
    challenge = Fifth(debug)
    challenge.one()
    challenge.two()


def sixth(debug):
    challenge = Sixth(debug)
    challenge.one()
    challenge.two()


def seventh(debug):
    challenge = Seventh(debug)
    challenge.one()
    # challenge.two()
    challenge.better_two()


if __name__ == '__main__':
    start(False)
