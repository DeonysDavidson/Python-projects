#number series 
from functools import reduce

#function for series 1
def series_1(l):
  x= reduce(lambda a,b : a+b, range(l))
  print(x)

#function for series 2
def series_2(l):
  x = 1
  print(x,end = ' ')
  
  for e in range(1,int(l/2)):
    x*=2
    print(x,end=' ')
    x*=1.5
    x = int(x)
    print(x,end=" ")


#function for series 3
def series_3(l):
  for e in range(1,l+1):
    print(e*e,end=' ')


#function for series 4
def series_4(l):
 for e in range(1,l+1):
   if e%2!=0:
     print(e**2,end=' ')
   else:
     print(e,end=' ')

#function for series 5
def series_5(l):
  count=1
  for e in range(1,l):
    if e%2!=0:
      print(e**2,end=' ')
    else:
      print(4+count,end=' ')
      count*=2

#function for series 6 
def series_6(l):
  for e in range(1,l+1):
    if e%2!=0:
      print(e**3,end=' ')
    else:
      print(e**2,end=' ')
    
def main():
  print('1. 1+2+3+4...\n2. 1,2,3,6,9,18,27,54...\n3. 1,4,9,16,25,36..\n4. 1,2,9,4,25,6,49..\n5. 1,5,9,6,25,8,49...\n6. 1,4,27,16,125.. ')
  ch = int(input('Enter the number of your choice :'))
  l = int(input('Enter the limit of the series :'))

  if ch==1:
    series_1(l)
  elif ch==2:
    series_2(l)
  elif ch==3:
    series_3(l)
  elif ch==4:
    series_4(l)
  elif ch==5:
    series_5(l)
  else:
    series_6(l)

main()
  
