l = ['Thiru - velchry','Thiru - porur','Thiru - roya','Thiru - koyam']
v = ['Bike','Auto','Mini','Micro','Prime']
for a,b in enumerate(l,1):
  print(a,b)
while True:
 loc = int(input('Enter the number of your selection :'))
 if loc>0 and loc<=len(l):
   break
 else:
   print('Selection Invalid')
for a,b in enumerate(v,1):
  print(a,b)
while True:
 veh = int(input('Enter the number of your selection :'))
 if veh>0 and veh<=len(v):
   break
 else:
   print('Selection Invalid')
cos = loc*100+veh*10
print('The cost is :Rs.',cos)
