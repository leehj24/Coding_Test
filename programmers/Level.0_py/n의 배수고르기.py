def solution(n, numlist):
    answer = []
    for i in numlist:
        if i%n==0:
            answer.append(i)
    return answer
#또는 
def solution(n, numlist):
    return [i for i in numlist if i%n==0]
# 배열 numlist의 원소중에 n의 배수를 나열
# n=3 , numlist=[1,2,3,4,5,6,7,8,9] , result=[3,6,9]