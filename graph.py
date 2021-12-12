class Graph:

    def __init__(self):
        self.root = None
        self.nodes = {}
        self.routes = []

    def get_all_small_caves(self):
        small_caves = []
        for node in self.nodes:
            if node.islower() and node != "start" and node != "end":
                small_caves.append(node)
        return small_caves

    def has_node(self, name):
        if name in self.nodes:
            return self.nodes[name]
        else:
            return None

    def add_node(self, name):
        new_node = Node(name)
        self.nodes[name] = new_node
        if self.root is None:
            self.root = new_node
        return new_node

    def find_paths(self):

        for node in self.nodes["start"].goes_to.items():
            self.traverse(node[1], ["start"])

        return self.routes

    def find_paths_rule_two(self):

        small_caves = self.get_all_small_caves()

        for small_cave in small_caves:
            for node in self.nodes["start"].goes_to.items():
                self.traverse_rule_two(node[1], ["start"], small_cave)

        return self.count_dedupe()

    def count_dedupe(self):
        dedupe = []
        for route in self.routes:
            item = ''.join(route)
            if item not in dedupe:
                dedupe.append(item)
        return len(dedupe)

    def traverse(self, node_in, current_route):

        if node_in.name == "end":
            self.routes.append(current_route)

        current_route.append(node_in.name)
        for node in node_in.goes_to.items():
            if node[1].name != "start":
                if self.should_revisit(node[1], current_route):
                    self.traverse(node[1], current_route.copy())

    def traverse_rule_two(self, node_in, current_route, small_cave_allowed_revisit):

        if node_in.name == "end":
            self.routes.append(current_route)

        current_route.append(node_in.name)
        for node in node_in.goes_to.items():
            if node[1].name != "start":
                if self.should_revisit_rule_two(node[1], current_route, small_cave_allowed_revisit):
                    self.traverse_rule_two(node[1], current_route.copy(), small_cave_allowed_revisit)

    @staticmethod
    def should_revisit(node, current_route):
        return node.name.isupper() or node.name not in current_route

    @staticmethod
    def should_revisit_rule_two(node, current_route, small_cave_allowed_revisit):

        if node.name.isupper():
            return True

        if node.name != small_cave_allowed_revisit:
            return node.name not in current_route

        return current_route.count(node.name) < 2


class Node:

    def __init__(self, name):
        self.name = name
        self.goes_to = {}

    def add_goes_to(self, goes_to):
        self.goes_to[goes_to.name] = goes_to