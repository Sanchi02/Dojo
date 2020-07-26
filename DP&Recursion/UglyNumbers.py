'''
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number.
'''

n = int(input())

def maxDiv(number, divisor):
    while(number%divisor == 0):
        number = number//divisor
    return number

counter = 0
num = 1
while(counter != n):
    flag = maxDiv(num, 2)
    flag = maxDiv(flag, 3)
    flag = maxDiv(flag, 5)
    if(flag == 1):
        counter += 1
    num += 1

print(num-1)