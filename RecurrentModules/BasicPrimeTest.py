import math

num = int(input())
isPrime = True
for i in range(2,int(math.sqrt(num))+1):
    if(num%i==0):
        isPrime = False
print(isPrime)
