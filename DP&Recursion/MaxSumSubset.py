# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
def isSubsetSum(arr,n, sum) : 
    if (sum == 0) :
        return True
    if (n == 0 and sum != 0) :
        return False
    if (arr[n - 1] > sum) :
        return isSubsetSum(arr, n - 1, sum)
    return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr, n-1, sum-arr[n-1])
	
arr = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(arr) 
if (isSubsetSum(arr, n, sum) == True) :
    print("Found a subset with given sum")
else : 
	print("No subset with given sum")

