def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1] # 현재 값과 이전 값의 차이를 계산
        if diff == 1:
            answer += 'w' # 1 더하기
        elif diff == -1:
            answer += 's' # 1 빼기
        elif diff == 10:
            answer += 'd' # 10 더하기
        elif diff == -10:
            answer += 'a' # 10 빼기
    return answer