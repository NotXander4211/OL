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
        validLens = [8, 16, 32, 64]
        b1 = [int(i) for i in b1]
        b1 = b1[::-1]
        b2 = [int(i) for i in b2]
        b2 = b2[::-1]
        if len(b1) not in validLens  or len(b2) not in validLens:
            raise KeyError("Bits too long/short bruh")
        s, c = [], []
        _s, _c = Adder.halfAdder(b1[0], b2[0])
        s.append(_s)
        c.append(_c)
        for bb1, bb2 in zip(b1[1:], b2[1:]):
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
    def binToHex(_bin: str) -> str:
        num = hex(int(_bin, 2))[2:]
        zf = len(num)
        if len(num) % 2 != 0:
            zf += 1
        num = num.zfill(zf)
        return f"0x{num}"
    @staticmethod
    def hexToBin(_hex: str) -> str:
        _hex = _hex[2:]
        return str(bin(int(_hex, 16)))[2:]
    @staticmethod
    def hexToDecimal(_hex: str) -> str:
        return str(int(_hex, 16))
    @staticmethod
    def binToDecimal(_bin: str) -> str:
        return str(int(_bin, 2))
        
# --------------- TESTS ---------------
# print(Adder.bit8Adder("00000011", "00000001"))
# print(Adder.signedBit8Adder("00000011", "10000001"))
# print(Helper.binToHex("111111111"))
# print(Helper.hexToBin("0xFF"))
