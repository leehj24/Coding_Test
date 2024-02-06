def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            answer.sort()
    if len(answer) == 0:
            answer.append(-1)
    return answer

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        answer = [-1]

    answer.sort()        
    return answer

#array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수
#divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
# arr               divisor     result
# [5, 9, 7, 10]	    5	        [5, 10]
# [3,2,6]	        10	        [-1]