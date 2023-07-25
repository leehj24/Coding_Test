def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i%2==0:
            answer.append(strArr[i].lower())
        else:
            answer.append(strArr[i].upper())
    return answer
#배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로, 
# 짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환함
