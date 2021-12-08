class SevenSegment:

    def __init__(self):
        self.number_maps = {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None
        }

        self.six_nine_or_zero = []
        self.two_three_or_five = []

    def add_to_map(self, map_position, connections):
        self.number_maps[map_position] = connections

    def add_to_six_nine_or_zero(self, connections):
        self.six_nine_or_zero.append(connections)

    def add_to_two_three_or_five(self, connections):
        self.two_three_or_five.append(connections)

    def work_out_missing_numbers(self):
        # work out 6
        for option in self.six_nine_or_zero:
            if len(set(self.number_maps[1]) - set(option)) > 0:
                self.number_maps[6] = option
        self.six_nine_or_zero.remove(self.number_maps[6])

        # work out 9 and 0
        if len(set(self.number_maps[4]) - set(self.six_nine_or_zero[0])) > 0:
            self.number_maps[0] = self.six_nine_or_zero[0]
            self.number_maps[9] = self.six_nine_or_zero[1]
        else:
            self.number_maps[9] = self.six_nine_or_zero[0]
            self.number_maps[0] = self.six_nine_or_zero[1]

        # work out 5
        for option in self.two_three_or_five:
            diff_six = set(self.number_maps[6]) - set(option)
            diff_nine = set(self.number_maps[9]) - set(option)

            if len(diff_six) == 1 and len(diff_nine) == 1 and diff_six != diff_nine:
                self.number_maps[5] = option
        self.two_three_or_five.remove(self.number_maps[5])

        # work out 2 and 3
        if len(set(self.number_maps[5]) - set(self.two_three_or_five[0])) == 2:
            self.number_maps[2] = self.two_three_or_five[0]
            self.number_maps[3] = self.two_three_or_five[1]
        else:
            self.number_maps[3] = self.two_three_or_five[0]
            self.number_maps[2] = self.two_three_or_five[1]

    def get_answer_from_output(self, outputs):
        answer = []
        for output in outputs:
            for counter in range(0, 10):
                if len(self.number_maps[counter]) == len(output):
                    if len(set(self.number_maps[counter]) - set(output)) == 0:
                        answer.append(str(counter))
        return int(''.join(answer))
