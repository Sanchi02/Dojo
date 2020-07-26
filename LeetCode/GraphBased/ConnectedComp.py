# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

# Example 1:

# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

#      0          3
#      |          |
#      1 --- 2    4 

# Output: 2
# Example 2:

# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

#      0           4
#      |           |
#      1 --- 2 --- 3

# Output:  1
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        arrF = [[i] for i in range(n)]
        # print(arrF)
        for e in edges:
            sub1 = []
            sub2 = []
            # print(arrF)
            for a in arrF:
                if(e[0] in a):
                    sub1 = a
                if((e[1] in a) and len(sub1)!=0):
                    sub2 = a
                    break
            for a in arrF:
                if(e[0] in a):
                    sub1 = a
                if((e[1] in a) and len(sub1)!=0):
                    sub2 = a
                    break
            if((len(sub1)>0 and len(sub2)>0)and sub1!=sub2):
                tmp = sub1 + sub2
                arrF.remove(sub1)
                arrF.remove(sub2)
                arrF.append(tmp)
        print(arrF)
        return len(arrF)