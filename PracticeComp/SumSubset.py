
def printAllSubsetsRec(arr, n, v, sum) : 
    if (sum == 0) : 
        print(*v)
        return True
    
    if (n == 0 and sum !=0):
        return False
     
    if (n == 0):
        return True

    printAllSubsetsRec(arr, n - 1, v, sum)
    print("In function = {}".format(v))
    v1 = [] + v
    v1.append(arr[n - 1]) 
    tmp = printAllSubsetsRec(arr, n - 1, v1, sum - arr[n - 1])
    return tmp

arr = [ 2, 5, 8, 4, 6, 11 ] 
sum = 13
n = len(arr) 
v=[]
h = printAllSubsetsRec(arr, n,v, sum) 
print(h)
