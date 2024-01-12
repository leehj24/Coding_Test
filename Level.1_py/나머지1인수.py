def solution(n):
    for i in range(1,n):
        if n%i == 1:
            answer =i
            break
    return answer

# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

def solution(n):
    answer=0
    for i in range(1,n+1):
        if n%i == 0:
            answer += i
    return answer
