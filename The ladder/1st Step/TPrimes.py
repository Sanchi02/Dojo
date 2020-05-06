'''
We know that prime numbers are positive integers that have exactly two distinct positive divisors. Similarly, we'll call a positive integer t Т-prime, if t has exactly three distinct positive divisors.

You are given an array of n positive integers. For each of them determine whether it is Т-prime or not.

Input
The first line contains a single positive integer, n (1 ≤ n ≤ 105), showing how many numbers are in the array. The next line contains n space-separated integers x i (1 ≤ x i ≤ 1012).

Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is advised to use the cin, cout streams or the %I64d specifier.

Output
Print n lines: the i-th line should contain "YES" (without the quotes), if number x i is Т-prime, and "NO" (without the quotes), if it isn't.

'''

import math
rangeOfNum = 1000000

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

n = int(input())
for num in input().split():
    root = math.sqrt(int(num))
    if(int(root + 0.5) ** 2 == int(num)):
        root = int(root)
        if(sieve[root] == False):
            print('NO')
        else:
            print('YES')
    else:
        print('NO')



