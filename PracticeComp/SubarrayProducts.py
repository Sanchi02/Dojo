arr = list(map(int, input().split(' ')))
k = int(input())
arr.sort()
count = 0
print(arr)
for i in range(len(arr)):
    if(arr[i]<k):
        count += 1
        for j in range(i+1,len(arr)):
            if((arr[i]*arr[j])<k):
                count += 1
            else:
                break
    else:
        break
    
print(count)