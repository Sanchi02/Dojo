def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for _ in range(int(input())):
    num = int(input())
    arr = list(map(int, input().split(' ')))
    res = arr[0]
    for i in arr[1:]:
        res = gcd(res,i)
    print(res)
