def solution(arr):
    answer = 1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]!=arr[j][i]:
                answer = 0
    return answer

#특별한 이차원배열2