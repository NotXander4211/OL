#OL&fileio
#OL$LGFL str log.txt
#OL$LG bool 1
#OL!DB
#OL@IVS
#OL*

VAR func y fileio.read../src/logs/testtext.txt
VAR func nums fileio.add.2-2
VAR int x 10
PRINT __var_stack__
HALT