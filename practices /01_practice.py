def linearsearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i+1
    return -1
    

arr = [1,2,4,5,6,3,11,24,15]
target = int(input('enter the target'))
print(linearsearch(arr,target))