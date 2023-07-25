def solution(strArr):
    answer = []
    for i in strArr:
        if 'ad' in i: 
            continue
        else:
            answer.append(i)
    return answer
#strArr 배열 내의 문자열 중 "ad"라는 부분 문자열을 
# 포함하고 있는 모든 문자열을 제거하고 남은 문자열

#strArr=["star","admin","banana"] result=["star","banana"]