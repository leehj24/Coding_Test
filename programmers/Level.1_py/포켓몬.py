def solution(nums):
    div= len(nums)//2
    k = set(nums)
    answer= min(len(k),div)
    return answer


def solution(ls):
    return min(len(ls)/2, len(set(ls)))

# N / 2마리를 뽑는다고 했을 때 각자 다른 포켓몬이면 N / 2 종류의 포켓몬이 선택될 것이다.
# 그러나 중복 포켓몬이 많아서 N / 2 마리보다 적은 종류라면 그 종류 수 만큼이 선택할 수 있는 최대 종류의 수가 된다.
# nums result
# [3,1,2,3] 2
# [3,3,3,2,2,4] 3
# [3,3,3,2,2,2] 2
                        