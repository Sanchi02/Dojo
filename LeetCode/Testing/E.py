n = int(input())
arrA = [int(num) for num in input().split(' ')]
arrB = [int(num) for num in input().split(' ')]
arrC = []
for i in range(n):
    arrC.append(arrA[i]+arrB[i])
print(*arrC)