'''
Pashmak decided to give Parmida a pair of flowers from the garden. There are n flowers in the garden and the i-th of them has a beauty number b i. Parmida is a very strange girl so she doesn't want to have the two most beautiful flowers necessarily. She wants to have those pairs of flowers that their beauty difference is maximal possible!

Your task is to write a program which calculates two things:

The maximum beauty difference of flowers that Pashmak can give to Parmida.
The number of ways that Pashmak can pick the flowers. Two ways are considered different if and only if there is at least one flower that is chosen in the first way and not chosen in the second way.
Input
The first line of the input contains n (2 ≤ n ≤ 2·105). In the next line there are n space-separated integers b 1, b 2, ..., b n (1 ≤ b i ≤ 109).

Output
The only line of output should contain two integers. The maximum beauty difference and the number of ways this may happen, respectively.

'''

flowers = int(input())
beauty = []
for i in input().split():
    beauty.append(int(i))

maxB = max(beauty)
minB = min(beauty)
diff = abs(maxB - minB)
total = 0

if(maxB != minB):
    countMax = beauty.count(maxB)
    countMin = beauty.count(minB)
    print("{} {}".format(diff,countMax*countMin))
else:
    print("{} {}".format(diff,(flowers*(flowers-1))//2))
    