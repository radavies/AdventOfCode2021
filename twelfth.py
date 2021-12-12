from utils import read_input
from graph import Graph


class Twelfth:

    def __init__(self, debug):
        self.debug = debug
        self.input = read_input(self.debug, 12, self.line_function)
        print("---- Twelfth Challenge ----")

    def one(self):
        graph = self.setup_graph()
        paths = graph.find_paths()
        print("-- Part One --")
        print('Answer: {}\n'.format(len(paths)))

    def two(self):
        graph = self.setup_graph()
        path_count = graph.find_paths_rule_two()

        print("-- Part Two --")
        print('Answer: {}\n'.format(path_count))

    def setup_graph(self):
        graph = Graph()
        for line in self.input:
            new_node = graph.has_node(line[0])
            if new_node is None:
                new_node = graph.add_node(line[0])

            child = graph.has_node(line[1])
            if child is None:
                child = graph.add_node(line[1])

            new_node.add_goes_to(child)
            child.add_goes_to(new_node)
        return graph


    @staticmethod
    def line_function(line):
        return list(map(str.strip, line.split('-')))
