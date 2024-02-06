def solution(t,p):
    answer=[]
    count =0
    for i in range(len(t)-(len(p)-1)):
        answer.append(t[i:i+len(p)])
    for j in answer:
        if int(j)<=int(p):
            count +=1
    return count

def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer

#t와 p가 주어질 때, t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return
# t             p       result
# 3141592       271     3
# 500220839878  7       8
# 10203         15      3
#t="3141592"이고 p="271" 인 경우, t의 길이가 3인 부분 문자열은 314, 141, 415, 159, 592입니다. 이 문자열이 나타내는 수 중 271보다 작거나 같은 수는 141, 159 2개 입니다.