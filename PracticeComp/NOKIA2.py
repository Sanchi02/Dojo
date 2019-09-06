def recursion(l,r):
	if(r-l < 2):
		return 0
	elif (r-l == 0):
		return 2
	else:
		return r-l+recursion(l,l+(r-l)//2) + recursion(l+(r-l)//2,r)

for t in range(int(input())):
	n,m = map(int, input().split(' '))
	rw = recursion(0,n+1)
	ans = max(-1,m-rw)
	if ans != -1:
		ans = max(0,m-n*(n+3)//2)
	print(ans)
