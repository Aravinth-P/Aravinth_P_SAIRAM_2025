''' Greatest Common Divisor (GCD): Write a program to find the GCD of two integers using the Euclidean algorithm '''

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a,b=map(int,input().split())
print(gcd(a,b))

''' Integer Palindrome Check: Write a program that checks if a given integer is a palindrome. '''

n=input().strip()
if n==n[::-1]:
  print("palindrome")
else:
  print("Not a Palindrome")
