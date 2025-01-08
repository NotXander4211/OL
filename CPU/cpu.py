from cpumodule import *
mem = PersistentMemory()

class Register:
    def __init__(self, name, size):
        self.__size = size
        self.__value = "0" * size
        self.__name = name
        self.__subs = {name: [0, size]}
    def addSubs(self, register, start, end):
        self.__subs[register] = [start, end] 
    def getSubs(self, register):
        s = self.__subs[register][0]
        e = self.__subs[register][1]
        return self.__value[s:e]
    def setReg(self, value):
        self.__value = value
    def setSubs(self, register, value):
        s = self.__subs[register][0]
        e = self.__subs[register][1]
        value = value.zfill(e-s)
        self.__value = self.__value[:s] + value + self.__value[e:]
class Cpu:
    def __init__(self):
        self.rax = Register("RAX", 16)
        self.rax.addSubs("EAX", 8, 16)
        self.r8 = Register("R8", 16)
        self.r8.addSubs("R8D", 8, 16)
        self.r9 = Register("R9", 16)
        self.r9.addSubs("R9D", 8, 16)
        self.r8.setSubs("R8D", "00000001")
        self.r9.setSubs("R9D", "00000010")
        self.r10 = "00000001"
        self.r11 = "00000010"
        # print("-"+self.rax.getSubs("RAX")+"-")
        # self.rax.setSubs("EAX", "1111")
        # print("-"+self.rax.getSubs("RAX")+"-")
    def add(self, R1, R2) -> None:
        # self.registers["RAX"] = Adder.bit8Adder(self.registers[R1], self.registers[R2])
        self.rax.setSubs("EAX", Adder.bit8Adder(self.__getattribute__(R1), self.__getattribute__(R2)))
        print(self.rax.getSubs("RAX"))
    def clock(self) -> None:
        pass
    def setReg(self, Register: str, Value: str) -> None:
        # self.registers[Register] = Value
        pass
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
c.add("r10", "r11")
# c.setReg("R8", "00000001")
# c.setReg("R9", "00000010")
# c.add("R8", "R9")
# print(c.registers)
