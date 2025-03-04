import sys
import cpu

def sendDebug(string, var):
    # print(string)
    pass

global Ruleset, filen, programL, ModulesUsed, ModulesImported, program, lt, linecount

filen = "test.cpu"
if len(sys.argv) >= 2:
    filen = sys.argv[1]

programL = []
with open(filen, "r") as file:
    programL = [line.strip() for line in file.readlines()]

program = []
linecount = 0
lt = {}
Ruleset = ""
def lex(line, tc):
    global Ruleset, filen, programL, ModulesUsed, ModulesImported, lt, linecount
    program = []
    args = line.split(" ")
    opcode = args[0].lower()
    sendDebug(f"--Lexer scan: {opcode}", Ruleset)
    if opcode == "":
        sendDebug("blank line cont", Ruleset)
        return []
    if opcode.endswith(":"):
        lt[opcode[:-1]] = linecount+1
        sendDebug("label':' cont", Ruleset)
        return []
    if opcode.startswith("??"):
        #this is a comment ^
        sendDebug("?? cont", Ruleset)
        return []

    program.append(opcode)
    tc += 1
    if opcode == "mov":
        program.append(args[1])
        program.append(args[2])
        tc += 2
    elif opcode == "prt":
        program.append(args[1])
        tc += 1
    elif opcode == "add":
        program.append(args[1])
        program.append(args[2])
        tc += 2
    return program
code = []
for line in programL:
    # print(line)
    x = lex(line, 0)
    for i in x:
        code.append(i)
# print(code)
def run(program, pc, c):
    # for line in program
    opcode = program[pc]
    pc += 1
    if opcode == "mov":
        reg = program[pc]
        val = program[pc+1]
        c.setReg(reg, cpu.Helper.hexToBin(val))
        pc += 2
    elif opcode == "prt":
        reg = program[pc]
        print(c.getReg(reg))
        pc += 1
    elif opcode == "add":
        reg = program[pc]
        reg2 = program[pc + 1]
        c.add(reg, reg2)
        pc += 2
    elif opcode == "syscall":
        c.syscall()
    return pc
c = cpu.Cpu()
pc = 0
while code[pc] != "halt":
    pc = run(code, pc, c)
