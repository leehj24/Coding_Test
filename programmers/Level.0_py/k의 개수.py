def solution(i, j, k):
    answer = 0
    for n in range(i, j + 1):
        answer += str(n).count(str(k))
    return answer
#또는
def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer
#i와 j사이의 k의 숫자가 들어간 개수를 return
#i=1,j=13,k=1, result=6// 1이 들어간 숫자= 1,10,11,12,13