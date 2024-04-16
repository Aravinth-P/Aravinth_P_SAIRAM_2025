''' Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Example 1:
Input: s = "hello"
Output: "holle"
Example 2:
Input: s = "leetcode"
Output: "leotcede" '''


s=input().strip()
v=[]
for i in s:
    if i in "AEIOUaeiou":
        v.append(i)
v=v[::-1]
k=0
for i in s:
    if i in "AEIOUaeiou":
        print(v[k],end="")
        k+=1
    else:
        print(i,end="")
