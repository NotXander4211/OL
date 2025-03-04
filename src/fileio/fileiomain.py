def run(func, args):
    #print(args)
    returned = None
    match func.lower():
        case "read":
            returned = read(args)
        case "add":
            returned = add(args)
        case "readline":
            returned = readline(args)
        case "write":
            write(args)
        case "erase":
            erase(args)
        case "delete":
            delete(args)
        case "create":
            create(args)
    return returned

RETURNS = {"read":"list", "add":"int", "readline":"list", "write":"None", "erase":"None", "delete":"None", "create":"None"}


def listGet(lst, index, default, wtype):
    try:
        return wtype(lst[index])
    except IndexError:
        return default

def getReturnValue(funcName):
    return RETURNS[funcName]

def read(args):
    filename = args[0]
    #print(args)
    global line
    line = ""
    with open(filename, "r") as file:
        line = file.readlines()
        #print(line)
    return line

def readline(args):
    filename = args[0]
    with open(filename, "r") as file:
        lines = file.readlines()[listGet(args, 1, 0, int):listGet(args, 2, None, int)]
        return lines

def write(args):
    filename = args[0]
    with open(filename, "a") as file:
        file.write("".join(args[1:]) + "\n")

def erase(args):
    filename = args[0]
    with open(filename, "w") as _:
        pass

def delete(args):
    filename = args[0]
    __import__("os").remove(filename)

def create(args):
    filename = args[0]
    with open(filename, "w") as file:
        file.write(f"File {filename} successfully creates")

def add(args):
    return int(args[0]) + int(args[1])
        
        
