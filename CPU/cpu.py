from cpumodule import *
mem = PersistentMemory()

class Cpu:
    def __init__(self):
        self.registers = {"a": "10000000", "b": "01000000"}
    def add(self):
        self.registers["a"] = Adder.bit8Adder(self.registers["a"], self.registers["b"])
        self.registers["b"] = "00000000"
c = Cpu()
c.add()
print(c.registers)
