def check(arr1,arr2):
    answer = [[0 for _ in range(len(arr2[0]))]for _ in range(len(arr1))]
    print(answer)
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += (arr1[i][k]*arr2[k][j])
    return answer

def solution(A,B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

print(check([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
# 행렬의 곱을 구하여라

# 232 534     14  33
# 424 241     32  33
# 314 311     41  
# (2 * 5) + (3 * 2) + (2 * 3)