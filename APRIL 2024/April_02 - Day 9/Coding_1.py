''' 1. Two sum -Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example input: 
 nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. '''


k=[2,9,7,1]
t=9
n={}
def out(k,t):
    for i,j in enumerate(k):
        if t-j in n:
            return [n[t-j],i]
        else:
            n[j]=i
print(out(k,t))
