import sys

from module import *

# types: int, str, bool, list
# comment: ??
# #OL for commands
# #OL@ for other commands 
# #OL$ for bypass
# #OL@SS size<int>
# use that for stack size
# --not in bytes, in length of the stack<list>--
#default is 256 
#All commands are run during the lexing

global Ruleset, filen, programL, ModulesUsed, ModulesImported, program, lt, linecount

Ruleset = RuleSetConfigs(ss=256, vs=False)
filen = "./src/prog/anothertest.ol"
if len(sys.argv) >= 2:
    filen = sys.argv[1]

programL = []
with open(filen, "r") as file:
    programL = [line.strip() for line in file.readlines()]

ModulesUsed = []
ModulesImported = {}
program = []
linecount = 0
lt = {}

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
    # deal with #OL,  #OL@ for commands
    if opcode.startswith("#ol"):
        sendDebug("--Lexer: startswith #ol", Ruleset)
        permutator = opcode[3]
        cmd = opcode[4:]
        if permutator == "@": #rules 
            sendDebug("--Lexer: " + cmd.lower(), Ruleset)
            match cmd.lower():
                case "ss":         
                    Ruleset.setVal("ss", int(args[1]))
                case "ivs":
                    Ruleset.setVal("vs", True)
                case "evs":
                    Ruleset.setVal("vs", False)
        elif permutator == "!": #lexing
            match cmd.lower():
                case "db":
                    Ruleset.setVal("db", True)
                    sendDebug("Debug Active", Ruleset)
        elif permutator == "&": #imports:
            if cmd.lower() in ModuleLibrary:
                ModulesUsed.append(cmd.lower())
                sendDebug(f"Module imported: {cmd.lower()}", Ruleset)
        elif permutator == "$": #bypass
            if findType(args[1]) == bool:
                Ruleset.setVal(cmd.lower(), bool(int(args[2])))
            else:
                Ruleset.setVal(cmd.lower(), findType(args[1])(args[2]))
        elif permutator == "*":
            rulesInit(Ruleset)
        return []

    program.append(opcode)
    tc += 1
    if opcode == "push":
        #should give variable for now its only numbers(int)
        type_ = args[1]
        var = args[2]
        match type_.lower():
            case "int":
                program.append(int(var))
            case "str":
                program.append(str(var))
            case "bool":
                if var.lower() == "true":
                    program.append(True)
                else:
                    program.append(False)
            case "list":
                var = var.split(",")
                for i in range(len(var)):
                    var[i] = var[i].strip()
                program.append(var)
            case "var":
                program.append("_var_")
                program.append(str(var))
        tc += 1
    if opcode == "print":
        if args[1].lower() == "__top__":
            stringL = "__top__"
        elif args[1].lower() == "__stack__":
            stringL = "__stack__"
        elif args[1].lower() == "__var_stack__":
            stringL = "__var_stack__"
        else:
            stringL = " ".join(args[1:])[1:-1]
        program.append(stringL)
        tc += 1
    if opcode.startswith("jump"):
        label = args[1].lower()
        program.append(label)
        tc += 1
    if opcode == "var":
        type_ = args[1]
        var = args[3]
        varName = args[2]
        program.append(varName)
        tc += 1
        match type_.lower():
            case "int":
                program.append(int(var))
            case "str":
                program.append(str(var))
            case "bool":
                if var.lower() == "true":
                    program.append(True)
                else:
                    program.append(False)
            case "list":
                var = var.split(",")
                for i in range(len(var)):
                    var[i] = var[i].strip()
                program.append(var)
            case "func":
                program.append("func")
                tc += 1
                program.append(var)
                

        tc += 1
    return program, tc

ifseen = False
ifBlock = []
for line in programL:
    if line.split(" ")[0].lower().startswith("if"):
        ifseen = True
        ifBlock.append(line)
        continue

    if ifseen:
        if line.split(" ")[0].lower().startswith("endif"):
            ifseen = False
            ifBlock.append("endif")
            program.append(ifBlock)
            ifBlock = []
            linecount += 1
        else:
            curLine = lex(line, linecount)
            sendDebug(f"--Lexer: Curline: {curLine}", Ruleset)
            try:
                curLine[1]
            except:
                sendDebug(f"--Lexer: Curline Exception: {e}", Ruleset)
                continue
            for _code in curLine[0]:
                ifBlock.append(_code)
    else:
        curLine = lex(line, linecount)
        try:
            sendDebug(f"--Lexer: Curline: {curLine}", Ruleset)
            linecount += int(curLine[1])
        except Exception as e:
            sendDebug(f"--Lexer: Curline Exception: {e}", Ruleset)
            continue
        for _code in curLine[0]:
            program.append(_code)
    
#modules importing
for i in ModulesUsed:
    ModulesImported[i.lower()] = __import__(i.lower())


sendDebug(f"--Std Printer: {program}", Ruleset)
sendDebug(f"--Std Printer: {lt}", Ruleset)


stack = Stack(Ruleset.getVal("ss"), Ruleset.getVal("vs"))

def run(program, pc):
    global Ruleset, filen, programL, ModulesUsed, ModulesImported, lt, linecount, stack, opcode
    opcode = program[pc]
    sendDebug(f"--Runner: {opcode}", Ruleset)
    pc += 1
    if opcode == "push":
        if program[pc] == "_var_":
            pc += 1
            stack.push(stack.getVar(program[pc]))
            pc += 1
        else:
            stack.push(program[pc])
            pc += 1
    elif opcode == "pop":
        #will NOT save the value
        stack.pop()
    elif opcode == "read":
        num = int(input(""))
        stack.push(num)
    elif opcode == "print":
        if program[pc] == "__top__":
            strL = "TOP: " + str(stack.top())
        elif program[pc] == "__stack__":
            strL = "STACK: " + str(stack.buf) + " : " + str(stack.pt)
        elif program[pc] == "__var_stack__":
            strL = f"Var Stack: {str(stack.vars)}"
        else:
            strL = program[pc]
        print(strL)
        pc += 1
    elif opcode == "add":
        a = stack.pop()
        b = stack.pop()
        if CheckType(a, b, int, int):
            stack.push(a + b)
        else:
            raise EXCEPTIONS["TE"]("Top 2 variables in the stack are both not Type int")
    elif opcode.startswith("jump"):
        theTop = stack.top()
        sendDebug(f"--Runner 'jump' opcode: {type(stack.top())}", Ruleset)
        if JumpStatement(opcode, theTop):
            pc = lt[program[pc]]
        else:
            pc += 1
    elif opcode == "var":
        if program[pc + 1] == "func":
            sendDebug("Var-Func detected", Ruleset)
            mod = program[pc + 2].split(".")
            returned = moduleFuncRunner(mod, ModulesImported)
            functionModule = mod[0]
            functionName = mod[1]
            module = __import__(functionModule)
            returnType = module.getReturnValue(functionName)
            sendDebug(f"{returnType} {functionModule}.{functionName} returned {returned}", Ruleset)
            match returnType.lower():
                case "int":
                    stack.pushVar(program[pc], int(returned))
                case "str":
                    stack.pushVar(program[pc], str(returned))
                case "bool":
                    stack.pushVar(program[pc], bool(returned))
                case "list":
                    stack.pushVar(program[pc], list(returned))
                case "none":
                    stack.pushVar(program[pc], None)
                case _:
                    raise EXCEPTIONS["RTNV"](f"Return type of {returnType} is not valid")
            pc += 3
        else:
            stack.pushVar(program[pc], program[pc + 1])
            pc += 2
    elif len(mod := opcode.split(".")) >= 2:
        if mod[0].lower() not in ModulesUsed:
            raise EXCEPTIONS["MNI"](f"Module {mod[0].lower()} not imported")
        else:
            moduleFuncRunner(mod, ModulesImported)
            sendDebug(f"Module System Running: List of line args: {mod}", Ruleset)
            sendDebug(f"Arguments for Module {mod[0].lower()} function {mod[1].lower()}: {mod[2:]}", Ruleset)
    else:
        pc += 1
        raise EXCEPTIONS["OE"](opcode + "not implemented yet or not a possible opcode!")
    return pc

ifpc = 0
pc = 0

while program[pc] != "halt":
    if type(program[pc]) == list:
        #if statement
        block = program[pc]
        ifStatement = block[0]
        code = block[1:]
        if evaluateIfStatement(block, stack):
            while code[ifpc] != "endif":
                ifpc = run(code, ifpc)
            pc += 1
        else:
            pc += 1
    else:
        pc = run(program, pc)
    
sendDebug("--Runner: Complete", Ruleset)
