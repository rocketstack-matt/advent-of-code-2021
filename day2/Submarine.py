class Submarine:

    def __init__(self):
        self.horizontal_position = 0
        self.vertical_position = 0

    def forward(self, value: int):
        self.horizontal_position += value

    def up(self, value: int):
        self.vertical_position -= value

    def down(self, value: int):
        self.vertical_position += value

    def parse_instruction(self, instruction):
        instructions = instruction.strip().split()
        getattr(self, instructions[0])(int(instructions[1]))
