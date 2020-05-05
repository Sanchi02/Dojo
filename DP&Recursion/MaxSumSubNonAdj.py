def maxSubsetSum(arr):
    dp = []
    dp.append(arr[0])
    dp.append(max(arr[:2]))
    ans = max(dp)
    for a in arr[2:]:
        dp.append(max(max(dp[-2]+a, a), ans))
        ans = max(ans, dp[-1])
    print(dp)
    return ans	

# arr = list(input().split())
arr = [-2,1,3,-4,5]
print(maxSubsetSum(arr))