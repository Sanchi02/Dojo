def permutation(a,lower,upper):
    if(lower==upper):
        print(''.join(a))
    else:
        for i in range(lower,upper+1):
            a[lower],a[i] = a[i],a[lower]
            permutation(a,lower+1,upper)
            a[lower],a[i] = a[i],a[lower]

string = input()
permutation(list(string), 0, len(string)-1) 

