#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(Q):
    bribes = 0 
    Q = [P-1 for P in Q]
    print("Q")
    print(Q)
    print(list(enumerate(Q)))
    for i,P in enumerate(Q):
        print("New itr")
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
            print("j")
            print(j)
            if Q[j] > P:
                bribes += 1
    print(bribes)
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().split(' ')))
        minimumBribes(q)
