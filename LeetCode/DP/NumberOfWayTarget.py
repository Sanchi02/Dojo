# Python 3 Program to Count the number of ways to 
# construct the target string 

from collections import defaultdict

def recur(tracker, target,prev, arr):
	print("Target = {}, prev={}".format(target,prev))
	if(len(target)==0):
		arr.append(1)
		return
	tmp = tracker[target[0]]
	print("tmp = {}".format(tmp))
	for v in tmp:
		print("V = {}, prev = {}".format(v,prev))
		if(v[1]>prev[1]):
			recur(tracker, target[1:], v, arr)
	return arr

def countWays(a, s): 
	target = list(s)
	tracker = defaultdict(set)
	for i,w in enumerate(a):
		for j,c in enumerate(w):
			if(c in target):
				tracker[c].add((i,j))
	print(tracker)
	arr = recur(tracker,target, (-1,-1), [])
	return len(arr)
	 

# Driver Code 
if __name__ == '__main__': 
	A = [] 
	A.append("valya") 
	A.append("lyglb") 
	A.append("vldoh") 

	S = "val"

	print(countWays(A, S)) 