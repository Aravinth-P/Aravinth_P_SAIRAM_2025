''' You have write a function that accepts, a string which length is “len”, the string has some “#”, in it you have to move all the hashes to the front of the string and return the whole string back and print it.

Input:

Move#Hash#to#Front

Output:

###MoveHashtoFront '''


s=input().strip()
r,k="",""
for i in s:
    if i=="#":
        k+=i
    else:
        r+=i
print(k+r)
