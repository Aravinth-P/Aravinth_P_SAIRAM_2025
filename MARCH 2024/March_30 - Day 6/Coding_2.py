''' Find the power of a number without using pow() function. '''

a,b = map(int,input().split())
s=1
for i in range(b):
    s*=a
print(s)
