def solution(num_list, n):
    answer = []
    answer+=num_list[0::n]
    return answer
#num_list에 있는 배열을 n간격만큼 다시 추출
#num_list=[0,1,2,3,4,5,6,7] n=2 result=[0,2,4,6]