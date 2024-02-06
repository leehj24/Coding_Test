def solution(arr1, arr2):
    answer = arr1

    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer

def solution(A,B):   
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer

#  2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수
# arr1	         arr2	         return
# [[1,2],[2,3]]	 [[3,4],[5,6]]	 [[4,6],[7,9]]
# [[1],[2]]	     [[3],[4]]	     [[4],[6]]