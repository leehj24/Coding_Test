def solution(arr):

    arr.remove(min(arr))
    if len(arr) == 0:
        arr = [-1]
    return arr
# 배열 arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수
# arr           result
# [4,3,2,1]	    [4,3,2]
# [10]	        [-1]