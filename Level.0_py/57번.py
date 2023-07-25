def solution(num_list):
    answer = -1
    for i in num_list:
        if i<0:
            answer=num_list.index(i)
            break
    return answer

#num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록
#num_list=[12, 4, 15, 46, 38, -2, 15]	result=5