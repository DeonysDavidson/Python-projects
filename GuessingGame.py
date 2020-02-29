from random import randint
x=1
while(x<=5):
 print('Game %s of 5'%(x))
 s = randint(1,100)
 t = int(input('Guess a number between 1 and 100 :'))
 if t<s:
  print('guess was lower')
 elif t>s:
  print('guess was higher')
 else:
   print('guess was spot-on')
   break
 print('The number is :',s)
 x+=1

print('Game over')
