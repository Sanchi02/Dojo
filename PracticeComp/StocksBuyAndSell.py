prices = list(map(int, input().split(' ')))
localMinima = []
localMaxima = []

def getLocalMinMax(arr):
    Lmin = arr[0]
    Lmax = arr[0]
    t1,t2 = 0,0
    while(Lmin>arr[t1+1]):
        Lmin=arr[t1+1]
        t1 += 1
    localMinima.append(arr[t1])
    t2 = t1
    while(Lmax < arr[t2+1]):
        Lmax=arr[t2+1]
        t2 += 1
    localMaxima.append(arr[t2])
    return t2
    
lastInd = getLocalMinMax(prices)
