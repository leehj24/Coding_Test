def solution(to_list, finished):
    answer = []
    for i in range(len(finished)):
        if finished[i] ==False:
            answer.append(to_list[i])
    return answer

# to_list=['a', 'b', 'c', 'd']
# finished=['true','false','true','false']
# result = [b,d]