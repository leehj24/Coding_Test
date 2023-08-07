def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))
#또는
def solution(arr1, arr2):
    answer = 0
    if len(arr1)<len(arr2):
        answer=-1
    elif len(arr1)>len(arr2):
        answer=1
    elif len(arr1)==len(arr2) and sum(arr1)>sum(arr2):
        answer=1
    elif len(arr1)==len(arr2) and sum(arr1)<sum(arr2):
        answer=-1
    else:
        answer=0
    return answer

#두 배열의 길이가 다르면 배열의 길이가 긴 쪽이 더 크다
# 배열의 길이가 같다면 배열의 합의 크기가 큰 쪽이 크다
#정의한 배열의 대소관계에서 arr2가 크다면 -1, arr1이 크다면 1, 두 배열이 같다면 0 추출
#arr1[49, 13], arr2[70, 11, 2], result= -1
#arr1[1, 2, 3, 4, 5],, arr2[3, 3, 3, 3, 3], result=0