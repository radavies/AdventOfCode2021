class Bingo:

    def __init__(self):
        self.numbers_to_call = []
        self.boards = []
        self.board_marks = []

    def add_board(self, board):
        self.boards.append(board)
        self.board_marks.append([[False] * 5 for x in range(5)])

    def add_numbers_to_call(self, numbers_to_call):
        self.numbers_to_call = numbers_to_call

    def get_count_of_numbers_left_to_call(self):
        return len(self.numbers_to_call)

    def mark_boards(self):
        if len(self.numbers_to_call) < 1:
            raise Exception("Out of numbers to call")

        drawn_number = self.numbers_to_call.pop(0)
        board_counter = 0
        for board in self.boards:
            row_counter = 0
            for row in board:
                number_counter = 0
                for number in row:
                    if number == drawn_number:
                        self.board_marks[board_counter][row_counter][number_counter] = True
                    number_counter += 1
                row_counter += 1
            board_counter += 1

        return drawn_number

    def check_for_winners(self):
        board_counter = 0
        winning_boards = []
        for board in self.board_marks:
            if self.check_board_hor(board) or self.check_board_vert(board):
                winning_boards.append(board_counter)
            board_counter += 1
        return winning_boards

    def mark_boards_ignore_winners(self, previous_winners):
        if len(self.numbers_to_call) < 1:
            raise Exception("Out of numbers to call")

        drawn_number = self.numbers_to_call.pop(0)
        board_counter = 0
        for board in self.boards:
            if board_counter not in previous_winners:
                row_counter = 0
                for row in board:
                    number_counter = 0
                    for number in row:
                        if number == drawn_number:
                            self.board_marks[board_counter][row_counter][number_counter] = True
                        number_counter += 1
                    row_counter += 1
            board_counter += 1

        return drawn_number

    def check_for_winners_ignore_previous(self, previous_winners):
        board_counter = 0
        winning_boards = []
        for board in self.board_marks:
            if board_counter not in previous_winners:
                if self.check_board_hor(board) or self.check_board_vert(board):
                    winning_boards.append(board_counter)
            board_counter += 1
        return winning_boards

    def calculate_winning_score(self, winning_board_index, last_number_drawn):
        unmarked_total = 0
        line_counter = 0
        for line in self.board_marks[winning_board_index]:
            item_counter = 0
            for item in line:
                if item is False:
                    unmarked_total += self.boards[winning_board_index][line_counter][item_counter]
                item_counter += 1
            line_counter += 1

        return unmarked_total * last_number_drawn

    @staticmethod
    def check_board_hor(board):
        for line in board:
            line_is_all_marked = True
            for item in line:
                if item is False:
                    line_is_all_marked = False
                    break
            if line_is_all_marked:
                return True
        return False

    @staticmethod
    def check_board_vert(board):
        for item_counter in range(5):
            line_is_all_marked = True
            for vert_line_counter in range(5):
                if board[vert_line_counter][item_counter] is False:
                    line_is_all_marked = False
                    break
            if line_is_all_marked:
                return True
        return False
