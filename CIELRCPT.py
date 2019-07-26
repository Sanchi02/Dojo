powers = [1,2,4,8,16,32,64,128,256,512,1024,2048]

def deducter(moneyLeft):
    highestItem = 0
    for i in range(len(powers)):
        if(powers[i]>p):
            highestItem = i-1
            break
        if(i==len(powers)-1):
            highestItem = len(powers)-1
    return(p-powers[highestItem])

for t in range(int(input())):
    p = int(input())
    menuCount = 0
    for i in range(len(powers)):
        if(powers[i]>p):
            highestItem = i-1
            break
    while(p!=0):
        menuCount += 1
        p = deducter(p)
    print(menuCount)