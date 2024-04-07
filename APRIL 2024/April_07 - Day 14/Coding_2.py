''' Given an array of integers, where all elements but one occur twice, find the unique element.

Example:
 Input:[1,2,3,4,3,2,1]
Output:
4 '''


n = list(map(int,input().split()))
for i in n:
    if n.count(i)==1:
        print(i)
