''' 1.Given an array form a triangle such that the last row of the triangle contains all the elements of the array and the row above it will contain the sum of two elements below it.

Sample Input

arr[] = {4, 7, 3, 6, 7};

Sample Output

81
40 41
21 19 22
11 10 9 13
4 7 3 6 7 '''


l=[4,7,3,6,7]
r=[]
r.append(l)
k=l
for i in range(len(l)-1):
    o=[]
    for j in range(1,len(k)):
        o.append(k[j-1]+k[j])
    r.append(o)
    k=o
for i in r[::-1]:
    print(*i)


