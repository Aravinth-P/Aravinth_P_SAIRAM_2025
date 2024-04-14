''' 1. Program to find an alphabet by vowel or consonant
    2. Dimaond star pattern printing '''


s=input().strip()
if s in "AEIOUaeiou":
  print(s,"is a vowel")
else:
  print(s,"is a consonant")
    


      *
     ***
    *****
   *******
  *********
   *******
    *****
     ***
      *

n=int(input())
a=1
for i in range(n):
    for _ in range(n-i+1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
for i in range(n-2,-1,-1):
    for _ in range(n-i+1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
