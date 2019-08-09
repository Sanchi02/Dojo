def permutation(a, lower, upper):
    if(lower==upper):
        permutations.append(''.join(a))
    else:
        for i in range(lower, upper+1):
            a[lower], a[i] = a[i], a[lower]
            permutation(a, lower+1, upper)
            a[lower], a[i] = a[i], a[lower]
        

for t in range(int(input())):
    n,m = map(int, input().split(' '))
    listy = ''
    permutations = []
    wires = []
    nummy = []
    for tmp in range(n):
        listy = listy + str(tmp+1)
    permutation(list(listy), 0, n-1)
    # print(permutations)
    for p in permutations:
        p1 = list(p)
        start = 1
        end = n
        wire = m
        for val in p1:
            val1 = int(val)
            L = val1+1-start
            R = end+1-val1
            wire = wire-L-R
            if(L==1):
                start += 1
            if(R==1):
                end -= 1
        if(wire > 0 or wire==0):
            nummy.append(p)
            wires.append(wire)
    print(nummy)
    print(wires)    
    if(len(wires) == 0):
        print(-1)
    else:
        print(max(wires))
        
        