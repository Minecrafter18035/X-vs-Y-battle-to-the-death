z = 0
print ('x vs y ')
print ('')
while z != 3 :
  import random
  x = random.randint(0,10)
  y = random.randint(0,10)
  
  if x > y :
    print (str(z + 1) +'. ' 'X has defeated Y')
  elif x < y :
    print (str(z + 1) +'. ''Y has won')
  elif x == y :
    print (str(z + 1) +'. ''It is a tie this time')
    
  z += 1
