def solution(arr, intervals):
    answer = []
    for a,b in intervals: 
        answer+=arr[a:b+1]
    return answer

#arr=[1,2,3,4,5] intervals =[[1,3],[0,4]] result=[2,3,4,1,2,3,4,5]
#arr에 intervals 구간만큼 배열