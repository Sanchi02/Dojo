# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
def isSubsetSum(arr,n, sum,v) : 
    if (sum == 0) :
        print(v)
        return True
    if (n == 0 and sum != 0) :
        return False
    if (arr[n - 1] > sum) :
        return isSubsetSum(arr, n - 1, sum,v)
    v1 = [] + v
    v1.append(arr[n-1])
    flag = isSubsetSum(arr, n-1, sum,v) or isSubsetSum(arr, n-1, sum-arr[n-1],v1)
    # return flag
	
arr = [ 2, 5, 8, 4, 6, 11 ] 
sum = 13
n = len(arr)
v = []
if (isSubsetSum(arr, n, sum,v) == True) :
    print("Found a subset with given sum")
else : 
	print("No subset with given sum")

