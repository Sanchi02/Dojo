
for t in range(int(input())):
    n,k = map(int,input().split(' '))
    weights = [int(wgt) for wgt in input().split()]
    chefItems = 0
    checkFlag = (n-k)>k
    if(checkFlag):
        chefItems = n-k
    else:
        chefItems = k
    weights.sort()
    weights.reverse()
    chefWgt = weights[0:chefItems]
    kidWgt = weights[chefItems:n]
    val = sum(chefWgt)-sum(kidWgt)
    print(val)

