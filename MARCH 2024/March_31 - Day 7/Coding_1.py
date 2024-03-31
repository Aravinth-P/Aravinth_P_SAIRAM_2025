''' Write a Program to Check if a number is an Armstrong number or not. '''

X=input().strip()
s=0
for i in X:
    s+=pow(int(i),3)
if int(X)==s:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
