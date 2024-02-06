def solution(n):
    return len([number for number in range(1, n+1) if n%number == 0])
#또는
def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.extend([(i, n//i)])
    return len(answer)
#숫자 a,b의 공배수가 숫자 n이 되는 (a,b)의 수를 return
#n=100 result=9 #(1, 100), (2, 50), (4, 25), (5, 20), (10, 10), (20, 5), (25, 4), (50, 2), (100, 1) 