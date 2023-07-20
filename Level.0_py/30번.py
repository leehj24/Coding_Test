def solution(arr, queries):
    answer = []
    for a, b in queries:
        arr[a], arr[b] = arr[b], arr[a]
    answer = arr
    return answer

# arr= [0,1,2,3,4] queries=[[0,3],[1,2],[1,4]]
# arr의 0번째와 3번째 바꾸고, arr의 1번째와 2번째 바꾸고, arr의 1번째와 4번째 바꾸기