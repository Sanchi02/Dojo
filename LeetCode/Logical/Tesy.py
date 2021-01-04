# arr = [5,4,3,2,6,7,8,9,2,1,3]

# def partition(arr, low, high):
#     p = low - 1
#     pivot = arr[high]
#     for i in range(low,high):
#         if(arr[i]<pivot):
#             p += 1
#             arr[p], arr[i] = arr[i],arr[p]

#     arr[p+1],arr[high] = arr[high],arr[p+1]
#     return p+1

# def quickSort(arr, low, high):
#     if(low<high):
#         part = partition(arr,low,high)
#         quickSort(arr, low, part-1)
#         quickSort(arr,part+1, high)

# print(arr)
# quickSort(arr, 0 , len(arr)-1)
# print(arr)


arr = [2,2,1]
m = 3
ptr1 = 0
ptr2 = 0
op = 9999
while(ptr1 <= ptr2 and ptr2 < len(arr)):
    tmp = sum(arr[ptr1:ptr2+1])
    if(tmp < m):
        ptr2 += 1
    elif( tmp > m):
        ptr1 += 1
    else:
        op = min(op, ptr2-ptr1+1)
        ptr1 += 1
        ptr2 += 1

if(op==9999):
    return -1
else:
    return op