class Parser:
    def __init__(self, file):
        self.file = file
        self.content = self.getstring()
        self.instructions = []
    def getstring(self):
        return [x.split("\n")[0] for x in open(self.file, "r").readlines()]
    def generate_instructions(self):
        x = 0
        while x < len(self.content):
            self.instructions.append(self.content[x])
            x += 1
        print(self.instructions)