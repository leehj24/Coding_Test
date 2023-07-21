def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1

#arr=[0,0,0,1] idx=1 result =3
#arr[idx]값이 1인 인덱스 값 추출