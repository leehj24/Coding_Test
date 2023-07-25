def solution(arr):
    answer = 0
    old = arr
    while(True):
        new = []
        for i in old:
            if i>=50 and i%2 == 0:
                i = i/2
            elif i<50 and i%2 == 1:
                i = i*2 + 1
            new.append(int(i))
        if old == new:
            break
        else:
            old = new
            answer += 1
    return answer

#수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 
# 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.

#이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때, 
# arr(x) = arr(x + 1)인 x가 항상 존재합니다. 
# 이러한 x 중 가장 작은 값을 return 
#arr=[1, 2, 3, 100, 99, 98]	,result=5