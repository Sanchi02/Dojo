for i in range(int(input())):
    N = int(input())
    if (N > 6):
        elements = [int(n) for n in input().split()]
        curr_num = 1
        is_loop_broken = False
        while (len(elements) != 0 and len(elements) != 1):
            if (elements[0] == curr_num and elements[len(elements)-1] == elements[0]):
                elements.pop(len(elements)-1)
                if(len(elements) != 0):
                    elements.pop(0)
                    if (elements[0] == curr_num+1):
                        if(curr_num+1 < 11):
                            curr_num += 1
                        else:
                            is_loop_broken = True
                            break
            else:
                is_loop_broken = True
                break
        if (len(elements) == 1 and elements[0] != curr_num):
            is_loop_broken = True
        if is_loop_broken:
            print("no")
        else:
            print("yes")
    else:
        print("no")
