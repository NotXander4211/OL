from cpumodule import *
mem = PersistentMemory()

class Cpu:
    def __init__(self):
        self.registers = {"RAX": "0" * 64,
                          "R8": "0" * 64,
                          "R9": "0" * 64,
                          "R10": "0" * 64,
                          "R11": "0" * 64,
                          "R12": "0" * 64,
                          "R13": "0" * 64,
                          "R14": "0" * 64,
                          "R15": "0" * 64,
                          "MAR": "0" * 64,
                          "MDR": "0" * 64}
    def add(self, R1, R2) -> None:
        self.registers["RAX"] = Adder.bit8Adder(self.registers[R1], self.registers[R2])
    def clock(self) -> None:
        pass
    def setReg(self, Register: str, Value: str) -> None:
        self.registers[Register] = Value
    def getReg(Register: str, byte=None, bit=None) -> str:
        if byte:
            pass
        else:
            pass
    def getMem(Address: str) -> str:
        pass
    def lenReg(Register: str) -> int:
        pass

c = Cpu()
c.setReg("R8", "00000001")
c.setReg("R9", "00000010")
c.add("R8", "R9")
print(c.registers)
