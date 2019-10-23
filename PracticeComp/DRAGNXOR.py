t = int(input())
for _ in range(t):
    n,a,b = map(int, input().split(' '))
    a,b = format(a,"b"),format(b,"b")
    a = a+"0"*(n-len(a))
    b = b+"0"*(n-len(b))
    countA = min(a.count('0'), b.count('1'))
    countB = min(a.count('1'), b.count('0'))
    count = countA+countB
    num = "1"*count
    num = num + "0"*(n-len(num))
    print(int(num,2))