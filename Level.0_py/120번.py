def solution(n):
    result = []
    for i in range(n):
        arr = [0] * n
        arr[i] = 1
        result.append(arr)
    return result
# n*n크기의 이차원 배열 arr를 return
# n= 3	result =[[1, 0, 0], [0, 1, 0], [0, 0, 1]]