''' Given an array of integers, write a function to return the maximum product of two numbers in the array.

Implement a function in any programming language to remove duplicates from an unsorted array using a hash set or dictionary for efficient lookup. '''


l=list(map(int,input().split()))
r=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        r.append(l[i]*l[j])
print(max(r))

l=list(map(int,input().split()))
s=set()
for i in l:
    s.add(i)
print(s)

