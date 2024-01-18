def solution(arr):
    answer=[]
    arr.append('')
    for i in range(len(arr)-1):
        if arr[i] !=arr[i+1]:
            answer.append(arr[i])
    return answer

def solution(s):
     return [s[i] for i in range(len(s)) if s[i] != s[i+1:i+2]]
#베열 arr에 연속되는 수를 하나만 남기고 전부 제거한후 return
# arr            return
# [1,1,2,3,4,4]  [1,2,3,4]
# [1,2,2,2,5,6]  [1,2,5,6]
