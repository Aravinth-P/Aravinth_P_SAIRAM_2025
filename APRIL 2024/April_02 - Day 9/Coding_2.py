''' 2. Divide two integers without using division, multiplication and modulus operators
Example input:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3. '''

a,b=map(int,input().split())
k=0
while a>=b:
    a-=b
    k+=1
print(k)
