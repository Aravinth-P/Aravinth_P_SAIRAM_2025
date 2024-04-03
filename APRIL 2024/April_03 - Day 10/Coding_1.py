''' Program to calculate distance between two points
     input:
         (x1,y1)=(3,4)    (x2,y2)=(7,7)
     output: 5 '''

import math
a,b,c,d=map(int,input().split())
x=a-c
y=b-d
print(math.sqrt((x*x)+(y*y)))
