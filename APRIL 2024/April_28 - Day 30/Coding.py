''' 1.Write a  Program to check if two numbers are equal without using the bitwise operator.
    2. Write a Program to print sums of all subsets in an array. '''

a,b=map(int,input().split())
print("Same" if (a^b)==0 else "Not Same")


import itertools
l=list(map(str,input().split()))
for i in range(len(l)):
    for j in list(itertools.combinations(l,i+1)):
        s=0
        k=''.join(j)
        for u in k:
            s+=int(u)
        print(s)
