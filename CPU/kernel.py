from cpumodule import *

class Kernel:
    def __init__(self):
        self.syscallTbl = {}
        self.fdTbl = {0: "stdin", 1: "stdout"}
    def syscall(self):
        pass
k = Kernel()
