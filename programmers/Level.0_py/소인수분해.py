def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer
#숫자 n을 소인소분해한 숫자를 배열하여 return
#n=10 result=[2,5]