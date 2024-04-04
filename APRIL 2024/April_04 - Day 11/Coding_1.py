''' Write a Program to convert the binary number into a decimal number. '''

n = int(input())
b = bin(n)
print(b[2:])

n = int(input())
b = ""
while n>0:
    b+=str(n%2)
    n//=2
print(b[::-1])
