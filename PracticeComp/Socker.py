a,b,c = map(int, input().split(' '))
pairCounter = 0
sockArr = [1,1,1]
a,b,c = a-1,b-1,c-1
timesRemoved = 3

while(a!=0 or b!=0 or c!=0):
    # print("Values of a={} b={} c={}".format(a,b,c))
    # print("sockArr")
    # print(sockArr) 
    timesRemoved += 1
    index = 0
    # print("max(a,b,c) : {}".format(max(a,b,c)))
    # print("sockArr.count(0) : {}".format(sockArr.count(0)))
    if(sockArr.count(0)==0):
        if(max(a,b,c)==a):
            index=0
            a -= 1
        elif(max(a,b,c)==b):
            index=1
            b -= 1
        elif(max(a,b,c)==c):
            index=2
            c -= 1
        else:
            print("Error")
            break
    else:
        if(sockArr[0] == 0):
            if(a!=0):
                index=0
                a -= 1
            elif(b!=0):
                index=1
                b -= 1
            elif(c!=0):
                index=2
                c -= 1
        elif(sockArr[1] == 0):
            if(b!=0):
                index=1
                b -= 1
            elif(a!=0):
                index=0
                a -= 1
            elif(c!=0):
                index=2
                c -= 1     
        elif(sockArr[2] == 0):
            if(c!=0):
                index=2
                c -= 1
            elif(b!=0):
                index=1
                b -= 1
            elif(a!=0):
                index=0
                a -= 1
    sockArr[index] += 1
    # print("sockArr After")
    # print(sockArr) 
    if((sockArr[index])%2==0):
        sockArr[index] = 0
        pairCounter += 1
        print("To extract {} pairs, we need to remove a sock {} times".format(pairCounter, timesRemoved))
    
    