from functools import reduce

def skaiciuotidbd(x, y):
   while(y):
       x, y = y, x % y
   return x

def dbdkeliems(*skaiciai):
    return reduce(skaiciuotidbd, skaiciai)

def skaiciuotimbk(x, y):
   mbk = (x*y)//skaiciuotidbd(x,y)
   return mbk

def mbkkeliems(*skaiciai):
    return reduce(skaiciuotimbk, skaiciai)

s1 = 20
s2 = 32
s3 = 500
s4 = 9

print("DBD", dbdkeliems(s1, s2, s3, s4))
print("MBK", mbkkeliems(s1, s2, s3, s4))
