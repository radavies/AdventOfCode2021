class PathNode:

    def __init__(self, my_cost, coords, parent):
        self.total_cost = 0
        self.my_cost = my_cost
        self.coords = coords
        self.parent = parent

    # Compare nodes
    def __eq__(self, other):
        return self.coords == other.coords

    # Sort nodes
    def __lt__(self, other):
        return self.total_cost < other.total_cost
