from pathlib import Path


class DecemberSecond:

    debug = False
    instructions = None

    def __init__(self, debug):
        self.debug = debug
        self.instructions = self.get_instructions()

    def one(self):

        horizontal_pos = 0
        depth = 0

        for instruction in self.instructions:
            if instruction[0] == "forward":
                horizontal_pos += instruction[1]
            else:
                if instruction[0] == "up":
                    depth -= instruction[1]
                else:
                    depth += instruction[1]

        print(horizontal_pos)
        print(depth)
        print(horizontal_pos * depth)

    def two(self):
        horizontal_pos = 0
        depth = 0
        aim = 0

        for instruction in self.instructions:
            if instruction[0] == "forward":
                horizontal_pos += instruction[1]
                depth += (aim * instruction[1])
            else:
                if instruction[0] == "up":
                    aim -= instruction[1]
                else:
                    aim += instruction[1]

        print(horizontal_pos)
        print(depth)
        print(horizontal_pos * depth)

    def get_instructions(self):
        folder = Path("inputs")

        if self.debug:
            file = folder / "day2test.txt"
        else:
            file = folder / "day2.txt"

        data = open(file)
        instructions = []
        for line in data:
            split = str.split(line, " ")
            instructions.append([split[0], int(split[1])])
        data.close()

        return instructions
