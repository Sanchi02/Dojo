arr = [5,4,3,2,6,7,8,9,2,1,3]

def partition(arr, low, high):
    p = low - 1
    pivot = arr[high]
    for i in range(low,high):
        if(arr[i]<pivot):
            p += 1
            arr[p], arr[i] = arr[i],arr[p]

    arr[p+1],arr[high] = arr[high],arr[p+1]
    return p+1

def quickSort(arr, low, high):
    if(low<high):
        part = partition(arr,low,high)
        quickSort(arr, low, part-1)
        quickSort(arr,part+1, high)

print(arr)
quickSort(arr, 0 , len(arr)-1)
print(arr)