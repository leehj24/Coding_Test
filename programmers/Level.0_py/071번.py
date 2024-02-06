def solution(arr):
    answer = []
    for i in arr:
        if i >=50  and i%2==0:
            answer.append(int(i/2))
        elif i<=50  and i%2==1:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer

#arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 
# 2로 나누고, 50보다 작은 홀수라면 2를 곱합니다.