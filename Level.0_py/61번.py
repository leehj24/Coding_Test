def solution(num_list, n):
    answer = []
    for i in enumerate(num_list):
        answer = num_list[n-1::]
    return answer

#정수 리스트 num_list와 정수 n이 주어질 때, n 번째 원소부터 
# 마지막 원소까지의 모든 원소를 담은 리스트를 return하
# num_list=[5, 2, 1, 7, 5], n=2, result=[2, 1, 7, 5]