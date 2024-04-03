''' write a program to print the non repeated characters in the string.
    input:
       character
    output:
        h t e '''

s=input().strip()
for i in s:
    if s.count(i)==1:
        print(i,end=" ")
