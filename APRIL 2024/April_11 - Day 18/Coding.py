''' 1. Program to check whether given year is leap year or not
    2. Find the HCF (Highest Common Factor) of 2 number '''


n = int(input())
if n%400==0 or (n%100!=0 and n%4==0):
    print(n,"is a leap year")
else:
     print(n,"is not a leap year")


def gcd(m,n):
    if m<n:
        m,n = n,m
    while m%n!=0:
        m,n = n,m%n
    return n

a,b=map(int,input().split())
print(gcd(a,b))
