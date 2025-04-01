n = input()
k = list(map(int,n.split()))

chess= [1,1,2,2,2,8]
a =[]
for i in range(len(chess)):
    if k[i]!=chess[i]:
        a.append(str(chess[i]-k[i]))
    else:
        a.append('0')

print(" ".join(a))