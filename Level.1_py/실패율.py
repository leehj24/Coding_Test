def coke(N,stages):
    People = len(stages)
    faillist = {}
    for i in range(1, N + 1):
        if People != 0:
            faillist[i] = stages.count(i) / People
            People -= stages.count(i)
        else:
            faillist[i] = 0

    return sorted(faillist, key=lambda i: faillist[i], reverse=True)

print(coke(5,[2, 1, 2, 6, 2, 4, 3, 3]))
#N	stages	result
#5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
#4	[4,4,4,4,4]	[4,1,2,3]