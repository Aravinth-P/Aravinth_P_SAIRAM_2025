''' 1). Write a Program to sort First half in Ascending order and the Second in Descending order.

2).Write a Program to print the Maximum and Minimum elements in an array. '''



n=int(input())
l=list(map(int,input().split()))
k=n//2
a,b=l[:k],l[k:]
print(sorted(a)+sorted(b,reverse=1))


n=int(input())
l=list(map(int,input().split()))
print(max(l),min(l))
