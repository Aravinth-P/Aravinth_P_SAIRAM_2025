''' Get an integer from the user and print lucky number if the sum of odd numbers in a number is even else print not lucky number.
Sample Input 1:                                           351
Output:                                                        Not lucky number      
Explanation:                                                 3+5+1=9.9 is not an even number

Sample Input 2:                                           5638
Output:                                                       Lucky number
Explanation:                                                5+3=8. 8 is an even number '''

n = input()
s=0
for i in n:
  s+=int(i)
if s%2==0:
  print("Lucky Number")
else:
  print("Not Lucky Number")

