
def generateAllBinaryStrings(n, arr, i): 

	if i == n: 
		print(arr)
		return
	
	arr[i] = 0
	generateAllBinaryStrings(n, arr, i + 1)
	arr[i] = 1
	generateAllBinaryStrings(n, arr, i + 1)

n = int(input())
arr = [None] * n
generateAllBinaryStrings(n, arr, 0)
