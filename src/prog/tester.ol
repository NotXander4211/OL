??bypass
#OL$LGFL str log.txt
#OL$LG bool 1

??builtins
#OL!DB
#OL@IVS

??start file
#OL*

VAR STR x new
VAR LIST y 1,2,3,4,5
PRINT __var_stack__
PUSH VAR y
PRINT __stack__
HALT