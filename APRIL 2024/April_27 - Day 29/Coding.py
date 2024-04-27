''' Write a Program to Find fibonacci series upto N '''

n = int(input())
l = [0,1]+[0]*(n-1)
for i in range(2,n+1):
    l[i]=l[i-1]+l[i-2]
print(*l)

''' Write a program to find Maximum and Minimum in a Set '''
l= list(map(int,input().split()))
s = set(l)
print(max(s),min(s))
