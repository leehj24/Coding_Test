#문자열 리스트 출력 <입력: ["a","b","c"]> <출력: "abc">
def solution(arr):
    answer = ''
    for i in range(len(arr)):
        answer += arr[i]
    return answer