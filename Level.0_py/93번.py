def solution(arr, flag):
    X = []
    for i in range(len(arr)):
        if flag[i]:
            X.extend([arr[i]] * (arr[i] * 2))
        else:
            X = X[:-arr[i]]
    return X

#flag가 true이면 X에서 arr[i]를 두번씩 추가하고 flase면 마지막  X에서 arr[i]개의 원소를 제거한다
#arr=[3,2,4,1,3] flag= [true,false,true,false,false] result=[3,3,3,3,4,4,4,4]