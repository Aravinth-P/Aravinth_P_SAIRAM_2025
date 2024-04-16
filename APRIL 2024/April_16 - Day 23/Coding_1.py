''' 1.Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false '''

import collections 
def out():
    s=input().strip()
    t=input().strip()
    if len(s)!=len(t):
        return False
    a=collections.Counter(s)
    a.subtract(collections.Counter(t))
    return all(i==0 for i in a.values())
print(out())
