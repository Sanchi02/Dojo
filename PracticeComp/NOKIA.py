import copy

def permutation(a,lower,upper,perm):
    if(lower==upper):
        tmp = copy.deepcopy(a)
        perm = perm.append(tmp)
    else:
        for i in range(lower,upper+1):
            a[lower],a[i] = a[i],a[lower]
            permutation(a,lower+1,upper, perm)
            a[lower],a[i] = a[i],a[lower]
        
for t in range(int(input())):
    n,m = map(int, input().split(' '))
    listy = ''
    perm = []
    inital_wall = []
    for tmp in range(n):
        listy = listy + str(tmp+1)
        inital_wall.append(0)
    inital_wall = inital_wall + ([0,0])
    inital_wall[0], inital_wall[len(inital_wall)-1] = 1,1

    permutation(list(listy), 0, n-1, perm)
    wires = []
    for p in perm:
        wall = copy.deepcopy(inital_wall)
        wire_remaining = m
        for val in p:
            val1 = int(val)
            L_wall = wall[:val1]
            L = len(L_wall) - 1 - L_wall[::-1].index(1)
            R_wall = wall[val1+1:]
            R = R_wall.index(1) + 1
            wire_remaining = wire_remaining -  (val1 -L) - R
            wall[val1] = 1
        if(wire_remaining>=0):
            wires.append(wire_remaining)
            if(wire_remaining==0):
                break
    if(len(wires) > 0):
        print(min(wires))
    else:
        print(-1)
        
        
        