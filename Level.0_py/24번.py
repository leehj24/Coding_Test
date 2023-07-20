def solution(num_list):
    num = 1
    for i in range(len(num_list)):
        num *= num_list[i]
    if num < sum(num_list)**2:
        answer = 1
    else:
        answer = 0
    return answer

#numlist[3,4,5,6] 일때 3*4*5*6 < (3+4+5+6)**2 answer = 1