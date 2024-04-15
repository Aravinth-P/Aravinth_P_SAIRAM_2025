''' 1.Write a program to replace all 0's with 1's in a number 
    2.Write a program to find the transpose of a matrix '''

n = input().strip()
k=n.replace("0","1")
print(k)


n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
print(list(zip(*l)))
