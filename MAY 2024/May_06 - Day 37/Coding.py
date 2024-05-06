4
* * * * 
 * * * 
  * * 
   * 
  * *
 * * *
* * * *


n=int(input())
r=[]
for i in range(n):
    print(" "*i+"* "*(n-i))
    r.append(" "*i+"* "*(n-i))
r=r[::-1]
r=r[1:]
for i in r:
    print(i)


5
* * * * * 
*       * 
*       * 
*       * 
* * * * *


n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
