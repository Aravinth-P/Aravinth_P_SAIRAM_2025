'''Program to check whether the given number is prime number or not'''

import math
def isprime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
      return False
  return True

n = int(input())
print(isprime(n))
