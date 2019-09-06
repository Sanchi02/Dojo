for t in range(int(input())):
    M,x,y = map(int,input().split(' '))
    cop_houses = [house1 for house1 in input().split(' ')]
    range1 = x * y
    house_list = []
    house_list = [test for test in range(1,101)]
    for cop in cop_houses:
        upper_bound = int(cop) + range1
        lower_bound = int(cop) - range1
        if(upper_bound > 100):
            upper_bound = 100
        if(lower_bound < 0):
            lower_bound = 0
        for house in range(lower_bound,upper_bound+1):
            if(house_list.count(house) != 0):
                house_list.remove(house)
    print(len(house_list))
