friends = int(input())
friends = friends + 1
total = 0
ways = 0
for i in input().split():
    total = total + int(i)

for j in range(1,6):
    if((total+j)%friends!=1):
        ways += 1

print(ways)

