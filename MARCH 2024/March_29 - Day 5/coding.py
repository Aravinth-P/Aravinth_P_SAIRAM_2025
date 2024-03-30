* 
* * 
* * * 
* * * * 
* * * * * 

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

        * 
      * * 
    * * * 
  * * * * 
* * * * * 

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

* * * * * 
  * * * *
    * * *
      * *
        *

for i in range(n):
    for j in range(1,i+1):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()

* * * * *
 * * * *
  * * *
   * *
    *

k=0 
for i in range(n,0,-1):   
    for j in range(k):  
        print(end=" ")
    k += 1 
    for j in range(0, i):  
        print("*",end=" ")              
    print()
