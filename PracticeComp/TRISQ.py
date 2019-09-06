def recursion(n):
    if(n<4):
        return 0
    else:
        return recursion(n-2)+(n//2)-1

for t in range(int(input())):
    n = int(input())
    print(recursion(n))