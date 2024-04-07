''' Binary and linear search '''


n = [5,7,8,3,66,2]
t = int(input())
for i in range(len(n)):
    if n[i]==t:
        print(i,"is found")
        break
else:
    print("number is not present")



n = [5,7,8,3,66,2]
t = int(input())


def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

r = binarySearch(n, t, 0, len(n)-1)

if r:
    print("Element is present at index " + str(r))
else:
    print("Not found")
