string = list(input())
vowels = ['a','e','i','o','u']
count = 0
tmpArr = []
# print(string)
for i in range(len(string)):
    for j in range(i,len(string)):
        if(string[j] not in vowels):
            break
    if(j==len(string)-1 and j-i>4):
        tmpArr.append(string[i:])
    elif(j-i>4):
        tmpArr.append(string[i:j])

for str1 in tmpArr:
    for t in range(4,len(str1)):
        tmp = set(str1[:t])
        # print(tmp)
        if(len(tmp)==5):
            count += 1
            break
    count += (len(str1)-t)
print(count)
# print(tmpArr)