from cpumodule import *
mem = PersistentMemory()

class Cpu:
    def __init__(self):
        self.registers = {"RAX": "0" * 64,
                          "MAR": "0" * 64,
                          "MDR": ["0" * 8 for _ in range(0, 8)]}
        # self.regList = ["RAX", "MAR", "MDR"]
        # for i in self.regList:
        #     self.registers[i] = "0" * 64
    def add(self, R1, R2):
        self.registers[R1] = Adder.bit8Adder(self.registers[R1], self.registers[R2])
    def clock(self):
        pass

c = Cpu()
c.add()
print(c.registers)
