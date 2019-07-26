import math

def primality(num):
    isPrime = True
    num = int(num)
    if(num==2):
        return(isPrime)
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            isPrime = False
            break
    return(isPrime)

def permutation(a,lower,upper):
    if(lower==upper):
        listOfAna.append(''.join(a))
    else:
        for i in range(lower,upper+1):
            a[lower],a[i] = a[i],a[lower]
            permutation(a,lower+1,upper)
            a[lower],a[i] = a[i],a[lower]

def checkNums(number):
    if(number[0]=='0' or number=='1'):
        return False
    else:
        return primality(number)

listOfAna = []
isPrime = True
string = list(input())
permutation(string, 0, len(string)-1)
dictOfSets = {}

for anagram in listOfAna:
    for i in range(1,len(anagram)-2):
        for j in range(i+1,len(anagram)-1):
            num1 = anagram[0:i]
            num2 = anagram[i:j]
            num3 = anagram[j:len(anagram)]
            if(checkNums(num1)==False or checkNums(num2)==False or checkNums(num3)==False):
                break
            else:
                key = int(num1)*int(num2)*int(num3)
                dictOfSets.update({key:[num1,num2,num3]})
print(dictOfSets)


