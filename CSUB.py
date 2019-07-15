for t in range(int(input())):
    n = int(input())
    string = str(input())
    count = 0
    for i in range(0,n):
        for j in range(i,n):
            if(string[i]==str(1) and string[j]==str(1)):
                count = count + 1
    print(count)

