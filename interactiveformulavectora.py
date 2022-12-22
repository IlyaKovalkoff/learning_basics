'2th demention [a]=math.sqrt((ax**2)+(ay**2))'
'3th demention [a]=math.sqrt((ax**2)+(ay**2)+(az**2))'
import math
ax = float (input ("Введите значение координат x:"))
ay = float (input ("Введите значение координат y:"))
az = float (input ("Введите значение координат z:"))
if az==0:
    a = math.sqrt((ax**2) + (ay**2))
    print ('Vector length in 2d =',a)
if az!=0:
    a = math.sqrt((ax**2)+(ay**2)+(az**2))
    print ('Vector length in 3d =',a) 