
for i in range(int(input())):
    stringy = list(input())
    isLapin = True
    half1, half2 = [],[]
    if(len(stringy)%2==0):
        mid = int(len(stringy)/2)
        half1 = stringy[0:mid]
        half2 = stringy[mid:len(stringy)]
    else:
        mid = int(len(stringy)/2)
        half1 = stringy[0:mid]
        half2 = stringy[mid+1:len(stringy)]
    half1.sort()
    half2.sort()
    for character in half1:
        if(half2.count(character)!=0):
            half2.remove(character)
        else:
            isLapin = False
            break
    if(isLapin and len(half2)==0):
        print("YES")
    else:
        print("NO")
        