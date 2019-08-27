import copy

def genHourGlass(arr):
    sums = []  
    for x in range(4):
        for y in range(4):
            sumtmp = 0
            sumtmp = arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x+1][y+1]+arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2]
            sums.append(sumtmp)
    return max(sums)
arr = []

for _ in range(6):
    arr.append(list(map(int, input().split(' '))))
    
print(arr)
tada = genHourGlass(arr)
print(tada)
    