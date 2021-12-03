from utils import read_input


class Third:

    debug = False
    logs = None

    def __init__(self, debug):
        self.debug = debug
        self.logs = read_input(self.debug, 3, self.line_function)
        print("---- Third Challenge ----")

    def one(self):

        bit_counter = self.get_bit_counts(self.logs)

        gamma_rate = []
        epsilon_rate = []
        for count_pair in bit_counter:
            if count_pair[0] > count_pair[1]:
                gamma_rate.append("1")
                epsilon_rate.append("0")
            else:
                gamma_rate.append("0")
                epsilon_rate.append("1")

        gamma_rate_string = ''.join(gamma_rate)
        epsilon_rate_string = ''.join(epsilon_rate)

        gamma_rate_int = int(gamma_rate_string, 2)
        epsilon_rate_int = int(epsilon_rate_string, 2)

        print("-- Part One --")
        print('Answer: {}\n'.format(gamma_rate_int * epsilon_rate_int))

    def two(self):
        oxy_list = self.logs
        co2_list = self.logs

        bit_pos_counter = 0
        while len(oxy_list) > 1:
            oxy_list = self.filter_oxy(oxy_list, bit_pos_counter)
            bit_pos_counter += 1

        bit_pos_counter = 0
        while len(co2_list) > 1:
            co2_list = self.filter_co2(co2_list, bit_pos_counter)
            bit_pos_counter += 1

        oxy_int = int(oxy_list[0], 2)
        co2_int = int(co2_list[0], 2)

        print("-- Part Two --")
        print('Answer: {}\n'.format(oxy_int * co2_int))

    def filter_oxy(self, list_to_filter, bit_pos_counter):
        bit_counter = self.get_bit_counts(list_to_filter)
        output_list = []
        for line in list_to_filter:
            # more 1s
            if bit_counter[bit_pos_counter][0] >= bit_counter[bit_pos_counter][1]:
                if line[bit_pos_counter] == "1":
                    output_list.append(line)
            # more 0s
            elif bit_counter[bit_pos_counter][0] < bit_counter[bit_pos_counter][1]:
                if line[bit_pos_counter] == "0":
                    output_list.append(line)

        return output_list

    def filter_co2(self, list_to_filter, bit_pos_counter):
        bit_counter = self.get_bit_counts(list_to_filter)
        output_list = []
        for line in list_to_filter:
            # more 1s
            if bit_counter[bit_pos_counter][0] >= bit_counter[bit_pos_counter][1]:
                if line[bit_pos_counter] == "0":
                    output_list.append(line)
            # more 0s
            elif bit_counter[bit_pos_counter][0] < bit_counter[bit_pos_counter][1]:
                if line[bit_pos_counter] == "1":
                    output_list.append(line)

        return output_list

    @staticmethod
    def get_bit_counts(list_to_count_from):
        bit_counter = []
        for x in range(0, len(list_to_count_from[0])):
            if list_to_count_from[0][x] != '\n':
                bit_counter.append(None)

        for line in list_to_count_from:
            bit_pos_counter = 0
            for char in line:
                if char != "1" and char != "0":
                    break
                if char == "1":
                    if len(bit_counter) == 0 or bit_counter[bit_pos_counter] is None:
                        bit_counter[bit_pos_counter] = [1, 0]
                    else:
                        bit_counter[bit_pos_counter][0] += 1
                else:
                    if len(bit_counter) == 0 or bit_counter[bit_pos_counter] is None:
                        bit_counter[bit_pos_counter] = [0, 1]
                    else:
                        bit_counter[bit_pos_counter][1] += 1

                bit_pos_counter += 1

        return bit_counter

    @staticmethod
    def line_function(line):
        return line
