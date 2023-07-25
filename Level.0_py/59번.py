def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]

#정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 
# 가장 작은 연속된 부분 배열을 return 함