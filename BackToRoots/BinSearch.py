numList = [1,2,3,4,5,6,7,8,9,20]

def binSearch(lower,upper,numList,num):
    if(upper>=lower):
        mid = int(lower+(upper-lower)/2)
        if(numList[mid]==num):
            return mid
        elif(numList[mid]>num):
            return binSearch(lower,mid-1,numList,num)
        else:
            return binSearch(mid+1,upper,numList,num)
    else:
        return -1
    
num = int(input())
indi = binSearch(0,len(numList)-1,numList,num)
print(indi)
    
