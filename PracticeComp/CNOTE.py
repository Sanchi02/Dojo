for i in range(int(input())):
    X,Y,K,N = map(int,input().split())
    length_required = Y-X
    flag = False
    if length_required >= 0:
        flag = True
    else:
        for _ in range(N):
            P, C = map(int, input().split())
            if (abs(length_required)<=P and C<=K):
                flag = True
    if flag:
        print("LuckyChef")
    else:
        print("UnluckyChef")