def run(func, args):
    #print(args)
    returned = None
    match func.lower():
        case "read":
            returned = read(args)
        case "add":
            returned = add(args)
    return returned

RETURNS = {"read":"str", "add":"int"}

def getReturnValue(funcName):
    return RETURNS[funcName]

def read(args):
    filename = args[0]
    #print(args)
    global line
    line = ""
    with open(filename, "r") as file:
        line = file.read()
        #print(line)
    return line

def add(args):
    return int(args[0]) + int(args[1])
        
        