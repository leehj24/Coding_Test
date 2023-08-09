def solution(num_list, n):
    answer = []
    answer = num_list[n:]+num_list[:n]
    return answer

#num_list의 n번째 이후의 인덱스 값과 그 전 값을 이어서 붙이
#num_list=[5, 2, 1, 7, 5], n=3, result=[7, 5, 5, 2, 1]