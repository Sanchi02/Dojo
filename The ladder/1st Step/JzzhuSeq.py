'''
Jzzhu has invented a kind of sequences, they meet the following property:


You are given x and y, please calculate f n modulo 1000000007 (109 + 7).

Input
The first line contains two integers x and y (|x|, |y| ≤ 109). The second line contains a single integer n (1 ≤ n ≤ 2·109).

Output
Output a single integer representing f n modulo 1000000007 (109 + 7).
'''
seq = []
x, y = map(int,input().split())
val = int(input())

seq.append(9999)
seq.append(x)
seq.append(y)
seq.append(y-x)
seq.append(-1*seq[1])
seq.append(-1*seq[2])
seq.append(-1*seq[3])

tmp = val%6
if(tmp==0):
    print(seq[6]%1000000007)
else:
    print(seq[tmp]%1000000007)
