def solution(arr, n):
    answer = []
    for i,j in enumerate(arr):
        if len(arr)%2 !=0:
            if i%2 ==0: 
                answer.append(j+n)
            else:
                answer.append(j)
        if len(arr)%2 ==0:
            if i%2 !=0: 
                answer.append(j+n)
            else:
                answer.append(j)   
    return answer
# 또는 
def solution(arr, n):
    if len(arr) % 2:
        for i in range(0, len(arr), 2):
            arr[i] += n
    else:
        for i in range(1, len(arr), 2):
            arr[i] += n

    return arr

#arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, 
# arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return
#arr= [49,12,100,276 33], n=27, result=[76,12,127,276,60]