''' 1. Finding the frequency of elements in an array 
2. Rotate string n times in clockwise directio '''


l=list(map(int,input().split()))
f={}
for i in l:
    f[i]=f.get(i,0)+1
for i,j in f.items():
    print(i,":",j)


s=input().strip()
n=int(input())
for i in range(n):
    s=s[-1]+s[:-1]
print(s)
