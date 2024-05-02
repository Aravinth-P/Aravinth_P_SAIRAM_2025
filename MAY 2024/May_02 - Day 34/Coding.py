''' 1. Accept a string and count number of vowels in it.
    2. Accept a string and count number of consonants in it  '''



s=input().strip()
v,c=0,0
for i in s:
    if i in "AEIOUaeiou":
        v+=1
    else:
        c+=1
print("Vowels : ",v)
print("Consonanths : ",c)
