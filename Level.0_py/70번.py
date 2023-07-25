def solution(arr, queries):
    for s,e in queries:
        for i in range(s,e+1):
            arr[i] +=1
    return arr

#각 query마다 순서대로 
# s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.