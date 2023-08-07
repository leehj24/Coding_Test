def solution(num_list):
    answer = sorted(num_list)
    return answer[:5]

#num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return
#num_list=[12,4,15,46,38,1,14], result=[1,4,12 14,15]