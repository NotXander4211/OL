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
    # def __getattr__(self, name: str) -> str:
    #     if name in self.__subs:
    #         return self.getSubs(name)
    # def __setattr__(self, name: str, value: str) -> None:
    #     if name in self.__subs:
    #         self.setSubs(name, value)
class Cpu:
    def __init__(self) -> None:
        self.rax = Register("RAX", 16)
        self.rax.addSubs("EAX", 8, 16)
        self.rax.setSubs("EAX", "11001100")
        self.r8 = Register("R8", 16)
        self.r8.addSubs("R8D", 8, 16)
        self.r9 = Register("R9", 16)
        self.r9.addSubs("R9D", 8, 16)
        self.r8.setSubs("R8D", "00000001")
        self.r9.setSubs("R9D", "00000010")
        self.r10 = "00000001"
        self.r11 = "00000010"
        self.__registers = {"RAX": self.rax, "EAX": lambda: self.rax.getSubs("EAX")}
        # print("-"+self.rax.getSubs("RAX")+"-")
        # self.rax.setSubs("EAX", "1111")
        # print("-"+self.rax.getSubs("RAX")+"-")
        # self.rax = Register("RAX", 16)
        # self.rax.addSubs("EAX", 8, 16)
        # self.rax.eax = "11001111"
    def add(self, R1: str, R2: str) -> None:
        # self.registers["RAX"] = Adder.bit8Adder(self.registers[R1], self.registers[R2])
        self.rax.setSubs("EAX", Adder.bit8Adder(self.__getattribute__(R1), self.__getattribute__(R2)))
        print(self.rax.getSubs("RAX"))
    def clock(self) -> None:
        pass
    def setReg(self, Register: str, Value: str) -> None:
        # self.registers[Register] = Value
        pass
    def getReg(self, Register: str) -> str:
        return self.__registers[Register]()
    def getMem(Address: str) -> str:
        pass
    def lenReg(Register: str) -> int:
        pass

print("START CPU")
c = Cpu()
x = c.getReg("EAX")
print(x)
# c.add("r10", "r11")
# c.setReg("R8", "00000001")
# c.setReg("R9", "00000010")
# c.add("R8", "R9")
# print(c.registers)
