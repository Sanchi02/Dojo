'''
Appleman has n cards. Each card has an uppercase letter written on it. Toastman must choose k cards from Appleman's cards. Then Appleman should give Toastman some coins depending on the chosen cards. Formally, for each Toastman's card i you should calculate how much Toastman's cards have the letter equal to letter on ith, then sum up all these quantities, such a number of coins Appleman should give to Toastman.

Given the description of Appleman's cards. What is the maximum number of coins Toastman can get?

Input
The first line contains two integers n and k (1 ≤ k ≤ n ≤ 105). The next line contains n uppercase letters without spaces — the i-th letter describes the i-th card of the Appleman.

Output
Print a single integer – the answer to the problem.
'''
import copy
n,k = map(int, input().split())
seq = list(input())

record = {}

for l in seq:
    if(l not in record):
        record.update({l:1})
    else:
        tmp = record.get(l)
        record.update({l:tmp+1})

record = sorted(record.items(), key=lambda x: x[1], reverse=True)

total = 0

if(n <= k):
    for entry in record:
        total = total + (entry[1] ** 2)
else:
    poppedVal = []
    finalDict = []
    while(True):
        if(record[0][1] <= k):
            k = k - record[0][1]
            finalDict.append(copy.deepcopy(record[0]))
            record.remove(record[0])
        else:
            finalDict.append((record[0][0], k))
            break

    for entry in finalDict:
        total = total + (entry[1] ** 2)
print(total)


        

        