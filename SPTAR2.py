mock = int(input())
while(mock != 0):
    num_list = [int(n) for n in input().split(' ')]
    stack_list =[]
    counter=1
    while(True):
        if(len(stack_list)==0 and len(num_list)==0):
           print("yes")
           break
        elif(len(stack_list)!=0 and stack_list[len(stack_list)-1] == counter):
           stack_list.pop(len(stack_list)-1)
           counter += 1
        elif(len(stack_list) != 0 and len(num_list)==0):
           print("no")
           break
        elif(num_list[0] == counter):
           num_list.pop(0)
           counter += 1
        elif(len(num_list)!=0):
           stack_list.append(num_list[0])
           num_list.pop(0)
    mock = int(input())