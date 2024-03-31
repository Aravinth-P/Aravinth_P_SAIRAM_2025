''' Check whether a number is a palindrome. '''
x=input()
if x==x[::-1]:
  print("Palindrome Number")
else:
  print("Not a Palindrome Number")
