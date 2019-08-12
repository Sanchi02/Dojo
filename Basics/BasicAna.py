import copy

# def permutation(a,lower,upper):
#     if(lower==upper):
#         print(''.join(a))
#     else:
#         for i in range(lower,upper+1):
#             a[lower],a[i] = a[i],a[lower]
#             permutation(a,lower+1,upper)
#             a[lower],a[i] = a[i],a[lower]
            
def permutationNum(a,lower,upper,perm):
    if(lower==upper):
        tmp = copy.deepcopy(a)
        perm = perm.append(tmp)
    else:
        for i in range(lower,upper+1):
            a[lower],a[i] = a[i],a[lower]
            permutationNum(a,lower+1,upper, perm)
            a[lower],a[i] = a[i],a[lower]

# string = input()
listy = [1,2,3]
perm = []
# permutation(list(string), 0, len(string)-1) 
permutationNum(listy, 0, len(listy)-1, perm) 
print(perm)

