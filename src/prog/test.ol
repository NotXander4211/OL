#OL!DB
#OL@SS 256
#OL@IVS
PUSH INT 1
PRINT __top__
VAR INT x 10
PUSH VAR x
PRINT __top__
JUMP.GT.2 L2
PRINT "Evaluated to False"
HALT
L2:
PRINT "Evaluated to True"
HALT