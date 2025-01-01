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
        b2 = [int(i) for i in b2]
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
        return "".join([str(i) for i in s])
        
# --------------- TESTS ---------------
# print(Adder.halfAdder(1, 0))
# print(Adder.halfAdder(0, 1))
# print(Adder.halfAdder(1, 1))
# print(Adder.halfAdder(0, 0))
# print(Adder.fullAdder(1, 1, 1))
# print(Adder.fullAdder(0, 0, 0))
# print(Adder.fullAdder(1, 0, 0))
# print(Adder.fullAdder(0, 1, 0))
# print(Adder.fullAdder(0, 0, 1))
# print(Adder.fullAdder(1, 1, 0))
# print(Adder.fullAdder(1, 0, 1))
# print(Adder.fullAdder(0, 1, 1))
print(Adder.bit8Adder("11010000", "10000000"))
