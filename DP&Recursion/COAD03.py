t = int(input())
arr = [0]*1001
def populate():
    for i in range(1,1001):
        if(i%2==0):
            arr[i]=min(arr[i-1]+1,arr[i//2]+2)
        else:
            arr[i] = arr[i-1]+1
populate()
for _ in range(t):
    n = int(input())
    print(arr[n])
    