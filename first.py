from utils import read_input


class First:

    debug = False
    depth_list = []

    def __init__(self, debug):
        self.debug = debug
        self.depth_list = self.get_depth_array()
        print("---- First Challenge ----")

    def one(self):
        counter = 0
        previous = 0
        larger_counter = 0
        for depth in self.depth_list:
            if counter > 0:
                if depth > previous:
                    larger_counter += 1
            counter += 1
            previous = depth

        print("-- Part One --")
        print('Answer: {}\n'.format(larger_counter))

    def two(self):

        counter = 0
        larger_counter = 0
        for depth in self.depth_list:
            current_window = self.get_window_total(counter)
            next_window = self.get_window_total(counter + 1)

            if current_window is None or next_window is None:
                break

            if next_window > current_window:
                larger_counter +=1

            counter += 1

        print("-- Part Two --")
        print('Answer: {}\n'.format(larger_counter))

    def get_window_total(self, start_index):
        if len(self.depth_list) < start_index + 3:
            return None

        window_total = 0
        for counter in range(start_index, start_index + 3):
            window_total += self.depth_list[counter]

        return window_total

    def get_depth_array(self):
        return read_input(self.debug, 1, int)
