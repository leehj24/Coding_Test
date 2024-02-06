def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(i)
    return answer
# 또는
def solution(arr):
    answer = []
    for num in arr:
        answer += [num] * num
    return answer

#원소 a만큼 반복하며 추가
#arr=[5, 1, 4]	result=[5, 5, 5, 5, 5, 1, 4, 4, 4, 4]