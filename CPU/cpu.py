from cpumodule import *
mem = PersistentMemory()

class Register:
    def __init__(self, name: str, size: int) -> None:
        self.__size = size
        self.__value = "0" * size
        self.__name = name
        self.__subs = {name: [0, size]}
    def addSubs(self, register: str, start: int, end: int) -> None:
        self.__subs[register] = [start, end] 
    def addMSubs(self, subs: dict[str, tuple]) -> None:
        for subN, subL in subs.items():
            s = subL[0]
            e = subL[1]
            self.addSubs(subN, s, e)
    def getSubs(self, register: str) -> str:
        s = self.__subs[register][0]
        e = self.__subs[register][1]
        return self.__value[s:e]
    def setReg(self, value: str) -> None:
        self.__value = value
        print(f"Value set to {value}")
    def setSubs(self, register: str, value: str) -> None:
        s = self.__subs[register][0]
        e = self.__subs[register][1]
        value = value.zfill(e-s)
        self.__value = self.__value[:s] + value + self.__value[e:]
    def getSubsList(self) -> dict:
        return self.__subs
class Cpu:
    def __init__(self) -> None:
        print("START CPU INIT")
        self.CREATE_REGISTERS()
        # TEMP CREATE_REGISTERS
        self.rax = Register("rax", 16)
        self.r8 = Register("r8", 16)
        self.r9 = Register("r9", 16)
        self.r10 = Register("r10", 16)
        self.rax.addSubs("eax", 8, 16)
        self.r8.addSubs("r8d", 8, 16)
        self.r9.addSubs("r9d", 8, 16)
        self.r10.addSubs("r10d", 8, 16)
        self.lst = ["RAX", "R8", "R9", "R10"]
        self.__registers = {} 
        for i in self.lst:
            for j in self.__getattribute__(i.lower()).getSubsList():
                self.__registers[j.lower()] = i.lower()              
        print(self.__registers)
        # END TEMP CREATE_REGISTERS
        print("END CPU INIT")

    def CREATE_REGISTERS(self):
        pass
    def add(self, R1: str, R2: str) -> None:
        self.setReg("EAX", Adder.bit8Adder(self.getReg(R1), self.getReg(R2)))
        # print(self.getReg("RAX"))
    def clock(self) -> None:
        pass
    def getReg(self, Register: str) -> str:
        Register = Register.lower()
        # print(self.__getattribute__(self.__registers.get(Register)).getSubs(Register))
        return self.__getattribute__(self.__registers.get(Register)).getSubs(Register)
    def setReg(self, Register: str, Value: str) -> None:
        Register = Register.lower()
        self.__getattribute__(self.__registers.get(Register)).setSubs(Register, Value)
    def getMem(Address: str) -> str:
        pass
    def lenReg(Register: str) -> int:
        pass

c = Cpu()
# c.setReg("R8D", "10001111")
print(c.getReg("RAX"))
print(c.getReg("EAX"))
c.setReg("EAX", "11111111")
print(c.getReg("EAX"))
print(c.getReg("RAX"))
c.setReg("R8D", "00000001")
c.setReg("R9D", "00000010")
print(c.getReg("R8D"), c.getReg("R9D"))
c.add("R8D", "R9D")
print(c.getReg("EAX"))
print(c.getReg("RAX"))
