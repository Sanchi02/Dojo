def binSearch(lower,upper,numList,num):
    ans = len(numList)
    while(upper>=lower):
        mid = int(lower+(upper-lower)/2)
        if(numList[mid]>num):
            ans = mid
            upper=mid-1
        else:
            lower=mid+1
    return ans

for t in range(int(input())):
    n = int(input())
    disks = [int(disk) for disk in input().split()]
    stackList = [disks[0]]
    for i in range(1,len(disks)):
        newCreatedFlag = True
        indi = binSearch(0,len(stackList)-1,stackList,disks[i])
        if(indi==len(stackList)):
            stackList.append(disks[i])
        else:
            stackList[indi] = disks[i]
    newList = []
    newList.append(len(stackList))
    newList += stackList
    print(*newList)

