arr = []
def coin_filler(n):
    if(n==1):
        return 1
    else:
        return coin_filler(n-1)+n
    
# print(coin_filler(6))
def coin_populator(ind):
    array = [999,1]
    for i in range(2,ind):
        array.append(array[i-1]+i)
    return array[1:]



# print(coin_populator(7))
def coinRowPredictor(coins):
    array = [999,1]
    i = 2
    while(array[len(array)-1]<coins):
        array.append(array[i-1]+i)
        i += 1
    print(array)
    if(array[len(array)-1]>coins):
        return len(array)-2
    return len(array)-1
    
print(coinRowPredictor(28))
    