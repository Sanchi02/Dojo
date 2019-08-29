# n,m = map(int, input().split(' '))

# operations = []
# arr = []
# for t in range(m):
#     tmp = list(map(int, input().split(' ')))
#     operations.append(tmp)

# for _ in range(n):
#     arr.append(0)
    
# for operation in operations:
#     for tm in range(operation[0]-1,operation[1]):
#         arr[tm] = arr[tm]+operation[2]
        
# print(max(arr))

n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list[x-1] += incr
    if((y)<=len(list)): list[y] -= incr
    print("list")
    print(list)
max = x = 0
for i in list:
   x=x+i
   if(max<x): max=x
print(max)