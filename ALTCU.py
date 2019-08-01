#http://codeforces.com/contest/343/problem/B

wires = list(input())
isTangled = False
if(len(wires)%2==0):
    mid = int(len(wires)/2)
    while(len(wires) != 0):
        if(wires[mid]==wires[mid-1]):
            wires.pop(mid)
            wires.pop(mid-1)
            mid = int(len(wires)/2)
        else:
            isTangled = True
            break
else:
    isTangled = True
if(isTangled):
    print("No")
else:
    print("Yes")
        
            
        