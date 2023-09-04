def solution(array, n):
    array.sort()
    temp = []
    for i in array :
        temp.append( abs(n-i) )
    return array[temp.index(min(temp))]

#또는
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

#array=[1,2,3,4] n=6 result=4
#array의 원소중에 n과 제일 가까운 수 인 수를 return