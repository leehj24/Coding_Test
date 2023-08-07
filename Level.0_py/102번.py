def solution(rank, attendance):
    selected = []
    for i, attend in enumerate(attendance):
        if attend:
            selected.append((rank[i], i))

    selected.sort()
    a, b, c = selected[:3]

    return 10000 * a[1] + 100 * b[1] + c[1]

#참여가능한 등수가 높은 3명을 선발후 높은순으로 a,b,c라 할때 10000*a+ 100*b+c를 return
#rank [3,7,2,5,4,6,1], attendance[false,true,true,true,true,false,false], result=20403