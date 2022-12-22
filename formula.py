#3*(x)^2 + 4*x - 5 = 0
import math
a = 3
b = -14
c = -50
multi = (b**2)
d = multi - (4*a*c) 
print (multi,'d=',d)
if d>0:
    x1= (-b + math.sqrt(d)) / (2*a)
    x2= (-b - math.sqrt(d)) / (2*a)
    print('x1 =',x1,'x2 =',x2)
if d==0:
    x= -b/(2*a)
    print(x)
if d<0:
    'expresion have no any roots'
    print( 'expresion have no any roots')
