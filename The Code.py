z = 0
xx = 0
yy = 0
aa = 0
bb = 0

print ('X vs Y ')
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

print (' ')
print ('A vs B ')
print ('')
while z != 6 :
  import random
  a = random.randint(0,100)
  b = random.randint(0,100)
  
  if a > b :
    print (str(z + 1) +'. ' 'A has defeated B')
    aa += 1
  elif a < b :
    print (str(z + 1) +'. ''B has won')
    yy += 1
  elif a == b :
    print (str(z + 1) +'. ''It is a tie this time')

  z += 1
if aa > bb :
  print ('A has won the entire championship!')
elif aa < bb :
  print ('B has won the entire championship!')
elif aa == bb :
  print ('No one has won :(')

