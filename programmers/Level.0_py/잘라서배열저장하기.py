def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]
#또는
def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n] )
    return answer

# my_str ="abc1Addfggg4556b", n=6, result=["abc1Ad", "dfggg4", "556b"]
# 문자열 my_str을 n만큼 잘라서 배열한 후 return