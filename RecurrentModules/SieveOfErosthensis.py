rangeOfNum = int(input())
primes = []
sieve = [True]*(rangeOfNum+1)
sieve[0] = False
sieve[1] = False
p = 2
while (p*p <= rangeOfNum):
    if(sieve[p] == True):
        for i in range(p+p, rangeOfNum+1, p):
            sieve[i] = False
    p += 1

for i in range(rangeOfNum+1):
    if(sieve[i] == True):
        primes.append(i)

print(primes)