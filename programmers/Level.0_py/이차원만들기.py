def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer
#num_list=[1,2,3,4,5,6,7,8] n=2 result=[[1.2],[3,4],[5,6],[7,8]]
#num_list에 있는 배열을 n만큼 묶어 다시 2차원 배열로 변경