import pickle
import os

class PersistentMemory:
    def __init__(self, ramSize=1, rom=[], filename="MEMORY.olb") -> None:
        self.fn = f"{os.environ['CPU_PATH']}/cpumodule/{filename}"
        self.loaded = False

        try:
            self.loadMem()
            self.loaded = True
        except Exception as e:
            print(e)
    
        if not self.loaded:
            self.__ram = ["00000000" for _ in range(0, ramSize)]
            self.__rom = tuple(rom)
            self.saveMem()
            
    def loadMem(self):
        with open(self.fn, "rb") as file:
            tmp = pickle.load(file)
            data = tmp
            self.__ram = data["ram"]
            self.__rom = data["rom"]
            
    def saveMem(self):
        with open(self.fn, "wb+") as file:
            pickle.dump({"ram": self.__ram, "rom": self.__rom}, file)
    def writeRam(self, address, value):
        try:
            self.__ram[address] = value
        except IndexError:
            raise IndexError(f"RAM address {address} out of bounds")
    def readRam(self, address):
        try:
            # print(self.__ram[address])
            return self.__ram[address]
        except IndexError:
            raise IndexError(f"RAM address {address} out of bounds")
    def readRom(self, address):
        try:
            # print(self.__rom[address])
            return self.__rom[address]
        except IndexError:
            raise IndexError(f"ROM address {address} out of bounds")
    def OVERWRITE_ROM(self, value=[]):
        self.__rom = tuple(value)
        self.saveMem()
    def catMem(self):
        print(f"RAM: {self.__ram}")
        print(f"ROM: {self.__rom}")
if __name__ == "__main__":
    # mem = PersistentMemory(5, ["00010010","00000011","00000001","10101010","11001000"])
    # mem.saveMem()
    # -----------------TESTS-------------------
    mem = PersistentMemory()
    x = mem.readRom(1)
    y = mem.readRam(1)
    mem.writeRam(1, "00000011")
    print(x)
    print(y)
    y = mem.readRam(1)
    print(y)
    while not (inp := input(">> ")) == "exit":
        print(inp)
        try:
            eval(inp)
        except Exception as e:
            print(e)
            

