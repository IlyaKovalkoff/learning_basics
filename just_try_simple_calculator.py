def _add(x,y):
    return x + y

def _subtract (x,y):
    return x - y

def _multiple (x,y):
    return x * y

def _devide (x,y):
    return x / y

def _devide_only_int (x,y):
    return x // y
print(''' SELECT  
1 - '+'
2 - '-'
3 - '*'
4 - '/' 
5 - '//' ''')

u = int(input('----->'))


if u < 1:
    print ('Y select wrong number') 


if u == 1:
    x = float(input('Select first number-->'))
    y = float(input('Select second number-->'))
    print ('EQUALS = ', float(_add(x,y)))        


if u == 2:
    x = float(input('Select first number-->'))
    y = float(input('Select second number-->'))
    print ('EQUALS = ', float(_subtract(x,y))) 


if u == 3:
    x = float(input('Select first number-->'))
    y = float(input('Select second number-->'))
    print ('EQUALS = ', float(_multiple(x,y))) 


if u == 4:
    x = float(input('Select first number-->'))
    y = float(input('Select second number-->'))
    print ('EQUALS = ', float(_devide(x,y))) 


if u == 5:
    x = float(input('Select first number-->'))
    y = float(input('Select second number-->'))
    print ('EQUALS = ', int(_devide_only_int(x,y))) 


if u > 5:
    print ('Y select wrong number')





print ('RESTART THE PROGRAM FOR REPEAT')