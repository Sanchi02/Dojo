# Given a chess board of order N x M and source points (s1, s2) and destination points (d1, d2). The task to find minimum number of moves required by the Knight to go to the destination cell.

# Input:
# The first line of input contains an integer T denoting the number of testcases. Then T test cases follow. Each test case contains two lines. The first line of each testcase contains two space separated integers N and M. Then in the next line are four space separated values s1, s2 and d1, d2.

# Output:
# For each testcase in a new line print the minimum number of moves required by the knight to go to the destination from the source. If no such move is possible print -1.

# Constraints:
# 1 <= T <= 100
# 1 <= N, M <= 25

# Example:
# Input:
# 2
# 4 7
# 2 6 2 4
# 7 13
# 2 8 3 4

# Output:
# 2
# 3

# Explanation:
# Testcase 1: One possible move for Knight is from 2, 6 to 4, 5 and then to 2, 4 which is our destination.]

# dim = input()
# arr = input()
dim = [4,7]
arr = [2,6,2,4]
# dim = list(map(lambda x: int(x), dim.split(' ')))
# arr = list(map(lambda x: int(x), arr.split(' ')))
# [4, 7]
# [2, 6, 2, 4]
Xmin = 1
Xmax = dim[0]
Ymin = 1
Ymax = dim[1]
Xcur = arr[0]
Ycur = arr[1]
Xtar = arr[2]
Ytar = arr[3]
done = False
que = []
count = 0
que.append([Xcur, Ycur, 0])
visited = [[False]*Ymax for i in range(Xmax)]
# print(visited)
visited[Xcur-1][Ycur-1] = True
while que:
    print(que)
    axis = que.pop(0)
    # print(axis)
    if axis[0] == Xtar and axis[1] == Ytar:
        count = axis[2]
        done = True
        break
    else:
        count = axis[2]+1
        if axis[0]+2 >= Xmin and axis[0]+2 <= Xmax and axis[1]+1 >= Ymin and axis[1]+1 <= Ymax and visited[axis[0]+2-1][axis[1]+1-1] == False:
            que.append([axis[0]+2, axis[1]+1, count])
            visited[axis[0]+2-1][axis[1]+1-1] = True
        if axis[0]+2 >= Xmin and axis[0]+2 <= Xmax and axis[1]-1 >= Ymin and axis[1]-1 <= Ymax and visited[axis[0]+2-1][axis[1]-1-1] == False:
            que.append([axis[0]+2, axis[1]-1, count])
            visited[axis[0]+2-1][axis[1]-1-1] = True
        if axis[0]-2 >= Xmin and axis[0]-2 <= Xmax and axis[1]+1 >= Ymin and axis[1]+1 <= Ymax and visited[axis[0]-2-1][axis[1]+1-1] == False:
            que.append([axis[0]-2, axis[1]+1, count])
            visited[axis[0]-2-1][axis[1]+1-1] = True
        if axis[0]-2 >= Xmin and axis[0]-2 <= Xmax and axis[1]-1 >= Ymin and axis[1]-1 <= Ymax and visited[axis[0]-2-1][axis[1]-1-1] == False:
            que.append([axis[0]-2, axis[1]-1, count])
            visited[axis[0]-2-1][axis[1]-1-1] = True
        if axis[0]-1 >= Xmin and axis[0]-1 <= Xmax and axis[1]+2 >= Ymin and axis[1]+2 <= Ymax and visited[axis[0]-1-1][axis[1]+2-1] == False:
            que.append([axis[0]-1, axis[1]+2, count])
            visited[axis[0]-1-1][axis[1]+2-1] = True
        if axis[0]-1 >= Xmin and axis[0]-1 <= Xmax and axis[1]-2 >= Ymin and axis[1]-2 <= Ymax and visited[axis[0]-1-1][axis[1]-2-1] == False:
            que.append([axis[0]-1, axis[1]-2, count])
            visited[axis[0]-1-1][axis[1]-2-1] = True
        if axis[0]+1 >= Xmin and axis[0]+1 <= Xmax and axis[1]+2 >= Ymin and axis[1]+2 <= Ymax and visited[axis[0]+1-1][axis[1]+2-1] == False:
            que.append([axis[0]+1, axis[1]+2, count])
            visited[axis[0]+1-1][axis[1]+2-1] = True
        if axis[0]+1 >= Xmin and axis[0]+1 <= Xmax and axis[1]-2 >= Ymin and axis[1]-2 <= Ymax and visited[axis[0]+1-1][axis[1]-2-1] == False:
            que.append([axis[0]+1, axis[1]-2, count])
            visited[axis[0]+1-1][axis[1]-2-1] = True
# print(visited)
if done:
    print(count)
else:
    print(-1)
