def solution(a,b):
    answer =0
    if a <b:
        for i in range(a,b+1):
            answer +=i
    else:
        for i in range(b,a+1):
            answer +=i
    return answer
    
def solution(a, b):
	return sum(range(min(a, b), max(a, b) + 1))
    
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다

