z = 0
while z != 3 :
  print ('x vs y ')
  print ('')
  
  import random
  x = random.randint(0,10)
  y = random.randint(0,10)
  
  if x > y :
    print ('X has defeated Y')
  elif x < y :
    print ('Y has won')
  elif x == y :
    print ('It is a tie this time')
    
  z += 1
