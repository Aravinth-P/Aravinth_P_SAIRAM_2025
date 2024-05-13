''' 1.You are given a string s, which contains stars *.
In one operation, you can:Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe". '''

def removeCharacters(s):
    stars_indices = [i for i, char in enumerate(s) if char == '*']  
    result = list(s) 

    for star_index in stars_indices:
        non_star_index = star_index - 1  
        while non_star_index >= 0 and result[non_star_index] == '*':
            non_star_index -= 1  
        if non_star_index >= 0:  
            result[non_star_index] = '*' 
            result[star_index] = '*'  

    return ''.join(char for char in result if char != '*')  
s = input()
print(removeCharacters(s))  # Output: "lecoe"


''' Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3. '''

l=list(map(int,input().split()))
a,b=0,0
for i in l:
    if i<0:
        a+=1
    else:
        b+=1
print(max(a,b))
