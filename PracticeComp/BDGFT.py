import math

for t in range(int(input())):
    stringy = list(input())
    count = 0
    for i in range(len(stringy)):
        for j in range(i+1,len(stringy)):
            tmp = stringy[i:j+1]
            if(tmp.count('0')==(tmp.count('1')*tmp.count('1'))):
                count +=1
    print(count)