import pickle

class PersistentMemory:
    def __init__(self, ramSize=1, rom=[], filename="MEMORY.olb") -> None:
        self.fn = filename
        self.loaded = False

        try:
            self.loadMem(self.fn)
            self.loaded = True
        except Exception as e:
            print(e)
    
        if not self.loaded:
            self.__ram = [0 for _ in range(0, ramSize)]
            self.__rom = tuple(rom)
            self.saveMem()
            
    def loadMem(self, fn):
        pass #load
    
    def saveMem(self, fn):
        pass #save
    def writeRam(self, address, value):
        try:
            self.__ram[address] = value
        except:
            pass
    def readRam(self, address):
        try:
            return self.__ram[address]
        except:
            pass
    def readRom(self, address):
        try:
            return self.__rom[address]
        except:
            pass
