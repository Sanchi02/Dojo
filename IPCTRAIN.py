# https://www.codechef.com/JULY17/problems/IPCTRAIN

import heapq as h
import math

for t in range(int(input())):
    numTrainers, campDays = map(int, input().split(' '))
    listy = []
    priorityHeap = []
    for i in range(numTrainers):
        di, ti, si = map(int, input().split(' '))
        listy.append([di,ti,si])
    listy = sorted(listy,key=lambda x:x[0])
    for day in range(1,campDays+1):
        while(len(listy) !=0 and listy[0][0]==day):
            for tmp in range(listy[0][1]):
                test = -1*listy[0][2]
                h.heappush(priorityHeap,test)
            listy.pop(0)
        if(len(priorityHeap)!=0):
            h.heappop(priorityHeap)
    print(abs(sum(priorityHeap)))
        
# Instead of adding stuff one by one ot heap we can just add number to maintain the number of times the value will stay in the heap. 
# Once the val is zero we can pop it off