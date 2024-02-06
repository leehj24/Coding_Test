def solution(arr, k):
    answer = []
    for i in arr:
        if k%2==0:
            answer.append(i+k)
        else:
            answer.append(i*k)
    return answer
#k가 홀수면 배열의 원소와 곱하고 짝수면 합하라
#arr[1,2,3,4] k=2 result=[3,4,5,6]