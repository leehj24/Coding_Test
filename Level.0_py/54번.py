def solution(start, end):
    answer = []
    for i in range(start,end-1,-1):
        answer.append(i)
    return answer
# start= 10 , end= 3 result=[10,9,8,7,6,5,4,3]