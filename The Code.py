z = 0
xx = 0
yy = 0
print ('x vs y ')
print ('')
while z != 3 :
  import random
  x = random.randint(0,100)
  y = random.randint(0,100)
  
  if x > y :
    print (str(z + 1) +'. ' 'X has defeated Y')
    xx += 1
  elif x < y :
    print (str(z + 1) +'. ''Y has won')
    yy += 1
  elif x == y :
    print (str(z + 1) +'. ''It is a tie this time')

  z += 1
if xx > yy :
  print ('X has won the entire championship!')
elif xx < yy :
  print ('Y has won the entire championship!')
elif xx == yy :
  print ('No one has won :(')
