
class TypeError(Exception):
    pass

class MissingArgumentError(Exception):
    pass

class RestrictedUse(Exception):
    pass

class OpcodeException(Exception):
    pass

class OutOfStackException(Exception):
    pass

EXCEPTIONS = {"TE":TypeError, "MAE":MissingArgumentError, "RU":RestrictedUse, "OE":OpcodeException, "OSE":OutOfStackException}

findType = lambda x: str if x == 'str' else bool if x == 'bool' else int 

class RuleSetConfigs:
    def __init__(self, **kwargs):
        self.rules = kwargs
    def getVal(self, val):
        return self.rules.get(val, None)
    def setVal(self, key, val):
        self.rules[key] = val
    def __repr__(self):
        return str(self.rules)

class Stack:
    def __init__(self, size, vars):
        self.varUse = False
        if vars:
            self.vars = {}
            self.varUse = True
        self.buf = [0 for _ in range(size)]
        self.pt = -1
    def push(self, value: int):
        self.pt += 1
        try:
            self.buf[self.pt] = value
        except IndexError as e:
            raise OutOfStackException("Attemped to push, stack is full. increase stack size")
    def pop(self):
        #print(self.buf[self.pt])
        val = self.buf[self.pt]
        self.pt -= 1
        return val
    def top(self):
        return self.buf[self.pt]
    def pushVar(self, var, value):
        if self.varUse:
            self.vars[var] = value
        else:
            raise RestrictedUse("VS was not set to True, variable stack was not created")
    def getVar(self, var):
        if self.varUse:
            return self.vars[var]
        raise RestrictedUse("VS was not set to True, variable stack was not created")

def CheckType(type1, type2, wantedType1, wantedType2):
    global boolType1,boolType2
    boolType1 = False
    boolType2 = False
    if type(type1) == wantedType1:
        boolType1 = True
    if type(type2) == wantedType2:
        boolType2 = True
    return boolType1 and boolType2

def JumpStatement(statement, top):
    res = False
    args = statement.split(".")
    args[1] = args[1].lower()
    # this is fine bc we only need args[2] for ints for now
    if len(args) >= 3:
        args[2] = int(args[2])
    match args[1]:
            case "eq":
                if top == args[2]:
                    res = True
            case "gt":
                if top >= args[2]:
                    res = True
            case "lt":
                if top <= args[2]:
                    res = True
            case "tr":
                #looks worse but needed bc will always evaluate to true if there is value, same for case "fa"
                if top == True:
                    res = True
            case "fa":
                if top == False:
                    res = True
            case _:
                raise MissingArgumentError("Missing argument for jump statement")
    return res

getLogFile = lambda x: x.getVal("lgfl") or "log.txt"
getLogLocation = lambda x: x.getVal("lgloc") or "./src/logs/"

def sendDebug(msg, rs: RuleSetConfigs): # rs = rule set
    if not rs.getVal("db"):
        return
    if rs.getVal("lg"):
        # logging.basicConfig(filename=logfile, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # logging.debug(msg)
        with open(f"{getLogLocation(rs)}{getLogFile(rs)}", "a") as lf:
            lf.write(f"{msg}\n") #log message to file 
        return
    print(msg)

def rulesInit(rs: RuleSetConfigs):
    if rs.getVal("lg"):
        if not rs.getVal("wlgfl"):
            with open(f"{getLogLocation(rs)}{getLogFile(rs)}", "w"):
                pass
    sendDebug(rs, rs)
