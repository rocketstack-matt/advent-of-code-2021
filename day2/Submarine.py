class Submarine:

    def __init__(self):
        self.horizontal_position = 0
        self.vertical_position = 0
        self.aim = 0
        self.depth = 0

    def forward(self, value: int):
        self.horizontal_position += value
        self.depth += (self.aim * value)

    def up(self, value: int):
        self.vertical_position -= value
        self.aim -= value

    def down(self, value: int):
        self.vertical_position += value
        self.aim += value

    def parse_instruction(self, instruction):
        instructions = instruction.strip().split()
        getattr(self, instructions[0])(int(instructions[1]))
