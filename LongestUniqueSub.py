stringy = list(input())
counter = 0
for i in range(len(stringy)):
    tmp = []
    tmp.append(stringy[i])
    for j in range(i+1, len(stringy)):
        if(stringy[j] in tmp):
            break
        else:
            tmp.append(stringy[j])
    if(len(tmp)>counter):
        counter = len(tmp)
print(counter)
