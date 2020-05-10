import copy

n = int(input())
stairs = list(input().split())
m = int(input())
boxes = []
for i in range(m):
    tmp = list(input().split())
    boxes.append(copy.deepcopy(tmp))

edgeList = []
i = 1
j = 1
ptr = 0

while(j!=int(stairs[n-1])):
    edgeList.append([i,j])
    if(j != int(stairs[ptr])):
        j += 1
    else:
        i += 1
        j += 1
    ptr += 1
edgeList.append([i,j])

ptr = 0
flag = False
for b in boxes:
    if(flag!=True):
        while((edgeList[ptr][0] <= int(b[0])) or (edgeList[ptr][1] <= int(b[1]))):
            ptr += 1
            if(ptr >= int(stairs[n-1])):
                flag = True
                break
    if(flag != True):
        print(edgeList[ptr][1] - 1)
        ptr += 1
        if(ptr >= int(stairs[n-1])):
            flag = True
    else:
        print(ptr)
        ptr += int(b[1])
    
# 5
# 1 2 3 4 4
# 7
# 2 1
# 1 1
# 1 1
# 1 1
# 1 1
# 1 1
# 1 1