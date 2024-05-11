''' 1.Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array. 
It is given that all array elements are distinct.

Note:-  l and r denotes the starting and ending index of the array.
Example 1:
Input:
n = 6
arr[] = 7 10 4 3 20 15
k = 3
Output : 
7
Explanation :
3rd smallest element in the given 
array is 7

 2. Remove all characters from the string except numbers and alphabets '''


n=list(map(int,input().split()))
k = int(input())
n.sort()
print(n[k-1])


n=input()
r=""
for i in n:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyz" or i in "0987654321":
        r+=i
print(r)
