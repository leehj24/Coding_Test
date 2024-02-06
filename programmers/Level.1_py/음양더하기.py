def solution(absolutes,signs):
    answer =0
    for i in range(len(absolutes)):
        if signs[i]==False:
            absolutes[i]=-absolutes[i]
        else:
            pass
        answer += absolutes[i]
    return answer

def solution(absolutes, signs):
    for i in range (len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)
    
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다