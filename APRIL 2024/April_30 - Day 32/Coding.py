''' .Write a program that allows users to either convert integers to roman numerals, or convert roman numerals to integers. '''

s=input().strip()
d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
pv = 0
su = 0
for i in s[::-1]:
    v=d[i]
    if v<pv:
        su-=v
    else:
        su+=v
    pv = v
print(su)


n= int(input())
result = n  
p = 2
while p * p <= n:
    if n % p == 0:
        while n % p == 0:
            n //= p
        result -= result // p
    p += 1
if n > 1:
    result -= result // n

print(result)
