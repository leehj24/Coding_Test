def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    while len(answer) < k:
        answer.append(-1)
    return answer[:k]
# arr 원소의 서로다른 k개수를 추출, 배열의 길이가 k보다 작으면 나머지 값은 전부 -1
#arr=[0,1,1,2,2,3], k=3, result=[0,1,2]
#arr[0,1,1,1,1], k=4, result=[0,1,-1,-1]