from utils import read_input


class Tenth:

    def __init__(self, debug):
        self.debug = debug
        print("---- Tenth Challenge ----")

    def one(self):
        lines = read_input(self.debug, 10, self.line_function)
        errors = []
        for line in lines:
            error = self.check_line(line)
            if error is not None:
                errors.append(error)
        score = self.score_errors(errors)
        print("-- Part One --")
        print('Answer: {}\n'.format(score))

    def two(self):
        lines = read_input(self.debug, 10, self.line_function)
        errors = []
        line_index = 0
        for line in lines:
            if self.check_line(line.copy()) is not None:
                errors.append(line_index)
            line_index += 1

        for error in errors:
            lines[error] = None

        line_scores = []
        for line in lines:
            if line is not None:
                line_scores.append(self.score_line(self.complete_line(line)))
        line_scores.sort()

        final_score = line_scores[((len(line_scores) - 1) // 2)]

        print("-- Part Two --")
        print('Answer: {}\n'.format(final_score))

    def complete_line(self, line):
        openers = []

        while len(line) > 0:
            char = line.pop(0)
            if self.is_opener(char):
                openers.append(char)
            else:
                opener = openers.pop()
                if not self.is_match(opener, char):
                    raise Exception("Mismatched pair found")

        return self.get_missing_closers(openers)

    def check_line(self, line):
        openers = []

        while len(line) > 0:
            char = line.pop(0)
            if self.is_opener(char):
                openers.append(char)
            else:
                opener = openers.pop()
                if not self.is_match(opener, char):
                    return char
        return None

    @staticmethod
    def get_missing_closers(openers):
        closers = []
        while len(openers) > 0:
            opener = openers.pop()
            if opener == '(':
                closers.append(')')
            elif opener == '[':
                closers.append(']')
            elif opener == '{':
                closers.append('}')
            else:
                closers.append('>')
        return closers

    @staticmethod
    def is_match(opener, closer):
        if opener == '(':
            return closer == ')'
        elif opener == '[':
            return closer == ']'
        elif opener == '{':
            return closer == '}'
        else:
            return closer == '>'

    @staticmethod
    def score_errors(errors):
        score = 0
        for error in errors:
            if error == ')':
                score += 3
            elif error == ']':
                score += 57
            elif error == '}':
                score += 1197
            else:
                score += 25137
        return score

    @staticmethod
    def score_line(line):
        score = 0
        for char in line:
            score = score * 5
            if char == ')':
                score += 1
            elif char == ']':
                score += 2
            elif char == '}':
                score += 3
            else:
                score += 4
        return score

    @staticmethod
    def is_opener(char):
        return char in ['(', '[', '{', '<']

    @staticmethod
    def line_function(line):
        return list(line.strip())
