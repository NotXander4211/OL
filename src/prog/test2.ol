#OL!DB
#OL@SS 256
#OL@IVS
VAR INT x 5
PUSH INT 3
PUSH VAR x
PRINT __var_stack__
PRINT __top__
JUMP.GT.4 L1
HALT
L1:
PRINT "HI"
HALT