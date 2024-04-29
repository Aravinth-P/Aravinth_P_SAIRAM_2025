''' Bubble sort
    Add even digits in a number '''


l=list(map(str,input().split()))
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
    print(l)


s=input().strip()
k=0
for i in s:
    if int(i)%2==0:
        k+=int(i)
print(k)
