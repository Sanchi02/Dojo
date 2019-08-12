import copy

def popper(a,b,n):
    if len(b)==0:
        return "Yes"
    for i in range(0,n):
        if len(a[i])>0 and a[i][0]==b[0]:
            a[i]=a[i][1:]
            if popper(a,b[1:],n)=="Yes":
                return "Yes"
            else:
                a[i]=[b[0]]+a[i]
    return "No" 

for t in range(int(input())):
    n = int(input())
    a = []
    for tmp in range(n):
        tmp1 = [int(num) for num in input().split(' ')]
        a.append(copy.deepcopy(tmp1)[1:])
    b = [int(op) for op in input().split(' ')]
    b = b[::-1]
    if n==1:
        if a[0]==b:
            print("Yes")
        else:
            print("No")
    else:
        print(popper(a,b,n))