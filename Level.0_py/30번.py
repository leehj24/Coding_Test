def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer
# arr= [0,1,2,4,3] queries= [[0,4,2],[0,3,2],[0,2,2]] result =[3,4,-1]
# queries = [s,e,k] , 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]