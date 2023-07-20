def solution(n):
    answer = []
    while n >1:
        answer.append(int(n))
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1  
    answer.append(1)
    return answer
# n이 짝수면 %2 홀수이면 3 * n + 1 을 계속 계산하여 결국 1로 만듦
