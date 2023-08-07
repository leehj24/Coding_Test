def solution(strArr):
    a=[0]*31
    for x in strArr: a[len(x)]+=1
    return max(a)
#또는
def solution(strArr):
    answer = [len(i) for i in strArr]
    tmp = []
    for i in set(answer):
        tmp.append(answer.count(i))
    return max(tmp)

#strArr의 원소의 길이가 같은 문자열끼리 그룹으로 묶었을때 가장 개수가 많은 그룹의 크기를 return
#strArr=["a","bc","d","efg","hi"]	result=2
