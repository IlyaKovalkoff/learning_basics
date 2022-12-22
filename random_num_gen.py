import random 

random_numbers = [random.randrange(1, 100, 1) for nmbr in range (1000)]
print ("Random number list : ", random_numbers)
nmbrs=[]
print('***************************************************************************************************************')
for nmbr in random_numbers:
    if nmbr % 7 == 0:
        nmbrs.append(nmbr)
print (nmbrs)
#print (len([x for x in [random.randrange(1, 100, 1) for nmbr in range (1000)] if x % 7 ==0]))    
  
