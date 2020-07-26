n = int(input())

count0 = 0
count1 = 0
maxRun = -1

for i in input().split():
    t = int(i)
    if(t == 1):
        count1 += 1
        if(count0 > 0):
            count0 -= 1
    else:
        count0 += 1
        if(count0 > maxRun):
            maxRun = count0

ans = count1 + maxRun
print(ans)