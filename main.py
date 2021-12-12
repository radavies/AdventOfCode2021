from first import First
from second import Second
from third import Third
from forth import Forth
from fifth import Fifth
from sixth import Sixth
from seventh import Seventh
from eighth import Eighth
from ninth import Ninth
from tenth import Tenth
from eleventh import Eleventh
from twelfth import Twelfth


def start(debug):
    first(debug)
    second(debug)
    third(debug)
    forth(debug)
    fifth(debug)
    sixth(debug)
    seventh(debug)
    eighth(debug)
    ninth(debug)
    tenth(debug)
    eleventh(debug)
    twelfth(debug)


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


def eighth(debug):
    challenge = Eighth(debug)
    challenge.one()
    challenge.two()


def ninth(debug):
    challenge = Ninth(debug)
    challenge.one()
    challenge.two()


def tenth(debug):
    challenge = Tenth(debug)
    challenge.one()
    challenge.two()


def eleventh(debug):
    challenge = Eleventh(debug)
    challenge.one()
    challenge.two()


def twelfth(debug):
    challenge = Twelfth(debug)
    challenge.one()
    challenge.two()


if __name__ == '__main__':
    start(False)
