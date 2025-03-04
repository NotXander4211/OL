#OL&fileio
#OL$LGFL str log.txt
#OL$LG bool 1
#OL!DB
#OL@IVS
#OL*

??VAR func y fileio.read../src/logs/testtext.txt
??VAR func line1 fileio.readline../src/logs/testtext.txt-1
??VAR func nums fileio.add.2-2
VAR int x 8
??PRINT __var_stack__

if var x greaterthan int 9
print "true"
endif
print "false"
HALT
