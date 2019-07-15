for t in range(int(input())):
    n = int(input())
    num_list = [int(num) for num in input().split(' ')]
    swap_flag = False
    pointer = 0
    for i in range(n-2,-1,-1):
        if(num_list[i]<num_list[i+1]):
            pointer = i
            temp = num_list[i]
            num_list[i] = num_list[i+1]
            num_list[i+1] = temp
            swap_flag = True
            break
    if(swap_flag == False):
        print("-1")
    else:
        num_list[pointer+1:] = sorted(num_list[pointer+1:])
        out = ""
        for num in num_list:
            out += str(num)
        print(out)

    