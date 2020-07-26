import copy

n = int(input())
coor = []

for i in range(n):
    tmp = input().split()
    coor.append(copy.deepcopy(tmp))

groups = []

while(len(coor) != 0):
    tmp = []
    x = [coor[0][0]]
    y = [coor[0][1]]
    tmp.append(coor[0])
    coor.pop(0)
    dup = copy.deepcopy(coor)
    for i in dup:
        if(i[0] in x):
            tmp.append(copy.deepcopy(i))
            if(i[1] not in y):
                y.append(copy.deepcopy(i[1]))
            coor.remove(i)
        elif(i[1] in y):
            tmp.append(copy.deepcopy(i))
            if(i[0] not in x):
                x.append(copy.deepcopy(i[0]))
            coor.remove(i)
    dup = copy.deepcopy(coor)
    for i in dup:
        if(i[0] in x):
            tmp.append(copy.deepcopy(i))
            if(i[1] not in y):
                y.append(copy.deepcopy(i[1]))
            coor.remove(i)
        elif(i[1] in y):
            tmp.append(copy.deepcopy(i))
            if(i[0] not in x):
                x.append(copy.deepcopy(i[0]))
            coor.remove(i)
    dup = copy.deepcopy(coor)
    for i in dup:
        if(i[0] in x):
            tmp.append(copy.deepcopy(i))
            if(i[1] not in y):
                y.append(copy.deepcopy(i[1]))
            coor.remove(i)
        elif(i[1] in y):
            tmp.append(copy.deepcopy(i))
            if(i[0] not in x):
                x.append(copy.deepcopy(i[0]))
            coor.remove(i)
    dup = copy.deepcopy(coor)
    for i in dup:
        if(i[0] in x):
            tmp.append(copy.deepcopy(i))
            if(i[1] not in y):
                y.append(copy.deepcopy(i[1]))
            coor.remove(i)
        elif(i[1] in y):
            tmp.append(copy.deepcopy(i))
            if(i[0] not in x):
                x.append(copy.deepcopy(i[0]))
            coor.remove(i)
    dup = copy.deepcopy(coor)
    for i in dup:
        if(i[0] in x):
            tmp.append(copy.deepcopy(i))
            if(i[1] not in y):
                y.append(copy.deepcopy(i[1]))
            coor.remove(i)
        elif(i[1] in y):
            tmp.append(copy.deepcopy(i))
            if(i[0] not in x):
                x.append(copy.deepcopy(i[0]))
            coor.remove(i)
    
    groups.append(copy.deepcopy(tmp))

print(len(groups)-1)

            
