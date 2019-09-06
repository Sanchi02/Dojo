import copy

row = int(input())
col = int(input())
pos = []
for i in range(row):
    tmp = [j for j in input().split(' ')]
    pos.append(copy.deepcopy(tmp))
print(pos)
# for tmp in pos:
#     print(tmp)
hor = []
ver = []
for r in range(row):
    for c in range(col):
       if(pos[r][c]=='1'):
           hor.append(r)
           ver.append(c)

hor.sort()
ver.sort()
mid = len(hor)//2
meetingPoint = [int(hor[mid]),int(ver[mid])]

distance = 0
for ro in range(row):
    for co in range(col):   
        if (pos[ro][co] == '1'):
                distance += abs(meetingPoint[0] - ro) + abs(meetingPoint[1] - co); 
print(distance)


     

        