1 
2 3 
4 5 6 
7 8 9 10 

k=1
for i in range(4):
    for j in range(i+1):
        print(k,end=" ")
        k+=1
    print()


      1 
     1 1 
    1 2 1 
   1 3 3 1 
  1 4 6 4 1 

from math import factorial

n = 5
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()
