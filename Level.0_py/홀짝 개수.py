def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

#홀짝개수를 배열로 나열
#num_list =[1,2,3,4,5] result=[2,3]