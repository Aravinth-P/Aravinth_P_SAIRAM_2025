''' 1.Write a program to find GCD of two numbers.
    2.Write a Python program to remove duplicates from a list '''


def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b=map(int,input().split())
print(gcd(a,b))



l=list(map(int,input().split()))
r=[]
for i in l:
    if i not in r:
        r.append(i)
print(*r)
