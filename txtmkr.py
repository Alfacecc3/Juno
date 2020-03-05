#txtmkr
x = open('txtpassedtotxtmkr.txt', 'r').read()
try:
    f = open('textoutForTxtmkr.txt', 'r')
    f.close()
    pass
except FileNotFoundError:
    f = open('textoutForTxtmkr.txt', 'w+')
    f.close()

lines = open('textoutForTxtmkr.txt', 'r').readlines()
del lines
w = open('textoutForTxtmkr.txt', 'w')
w.write(x)
w.close()
pass
