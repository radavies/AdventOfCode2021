from folding_puzzle import FoldingPuzzle


class Thirteenth:

    def __init__(self, debug):
        self.debug = debug
        print("---- Thirteenth Challenge ----")

    def one(self):

        puzzle = FoldingPuzzle(self.debug)
        puzzle.fold(False)
        answer = puzzle.count_dots()

        print("-- Part One --")
        print('Answer: {}\n'.format(answer))

    def two(self):

        print("-- Part Two --")
        puzzle = FoldingPuzzle(self.debug)
        puzzle.fold_to_end()


