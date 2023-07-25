def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))
#홀수인덱스 합과 짝수 인덱스 합중 큰 것을 추출
#num_list=[1,2,3,4,5] result=9