class Logic:
    def __init__(self):
        pass
    @staticmethod
    def xor(v1, v2):
        return (v1 or v2) and not (v1 and v2) 
class Adder:
    def __init__(self):
        pass 
    @staticmethod
    def halfAdder(b1, b2):
        _carry = int(b1 and b2)
        _sum = int(Logic.xor(b1, b2))
        return _sum, _carry
    @staticmethod
    def fullAdder(b1, b2, cin):
        _s1, _c1 = Adder.halfAdder(b1, b2)
        _s2, _c2 = Adder.halfAdder(_s1, cin)
        _carry = int(_c1 or _c2)
        _sum = int(_s2)
        return _sum, _carry
    @staticmethod
    def bit8Adder(b1: str, b2: str) -> str:
        b1 = [int(i) for i in b1]
        b1 = b1[::-1]
        b2 = [int(i) for i in b2]
        b2 = b2[::-1]
        if len(b1) > 8  or len(b2) > 8:
            raise KeyError("Bits too long bruh")
        s, c = [], []
        _s, _c = Adder.halfAdder(b1[0], b2[0])
        s.append(_s)
        c.append(_c)
        for bb1, bb2 in zip(b1[1:], b2[1:]):
            # print(bb1, bb2)
            # print(s, c)
            # print(bb1, bb2, c[-1])
            _s, _c = Adder.fullAdder(bb1, bb2, c[-1])
            s.append(_s)
            c.append(_c)
        s = s[::-1]
        return "".join([str(i) for i in s])
    @staticmethod
    def signedBit8Adder(b1: str, b2: str) -> str:
        b2 = ["0" if i == "1" else "1" for i in b2]
        b2[0] = "0" if b2[0] == "1" else "1"
        b2 = "".join(b2)        
        b2 = Adder.bit8Adder(b2, "00000001")
        print(b2)
        s = Adder.bit8Adder(b1, b2)
        return s
class Helper:
    def __init__(self):
        pass
    @staticmethod
    def binToHexAndBack(_bin="", _hex="", fromHex=True):
        if fromHex:
            _hex = _hex[2:]
            return bin(int(hex, 16))
        else:
            return hex(int(_bin, 2))
        
# --------------- TESTS ---------------
print(Adder.bit8Adder("00000011", "00000001"))
print(Adder.signedBit8Adder("00000011", "10000001"))
