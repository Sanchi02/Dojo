for i in range(int(input())):
    workers = int(input())
    salaries = [int(Wi) for Wi in input().split()]
    fin_num = 0
    while salaries.count(max(salaries)) != len(salaries):
        num = max(salaries)-min(salaries)
        fin_num += num
        max_sal = max(salaries)
        index = salaries.index(max_sal)
        for i in range(0,workers):
            if i != index:
                salaries[i] += num
    print(fin_num)

