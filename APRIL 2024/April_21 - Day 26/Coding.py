''' Write a Program to find the Maximum and minimum of two numbers without using any loop or condition. 
Write a Program for simple calculator. '''


a,b=map(int, input().split())
print(max(a,b))
print(min(a,b))


a,b,c=map(str,input().split())
a,b=int(a),int(b)
s={
  '+' : lambda a,b : a+b,
  '-' : lambda a,b : a-b,
  '*' : lambda a,b : a*b,
  '/' : lambda a,b : int(a/b)
}
print(s[c](a,b))



