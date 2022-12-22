'2th demention [a]=math.sqrt((ax**2)+(ay**2))'
'3th demention [a]=math.sqrt((ax**2)+(ay**2)+(az**2))'
import math
ax = 6
ay = -5
az = 0
if az==0:
    a = math.sqrt((ax**2) + (ay**2))
    print ('Vector length in 2d =',a)
if az!=0:
    a = math.sqrt((ax**2)+(ay**2)+(az**2))
    print ('Vector length in 3d =',a) 