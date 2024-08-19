from collections import Counter

def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    res = 0
    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            res += 1
    return res

# 롤케이크에 올려진 토핑들의 번호를 저장한 정수 배열 topping이 매개변수로 주어질 때, 
# 롤케이크를 공평하게 몇가지 맛 을 볼 수 있도록 자르는 방법의 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ topping의 길이 ≤ 1,000,000
# 1 ≤ topping의 원소 ≤ 10,000
# 입출력 예
# topping			result
# [1, 2, 1, 3, 1, 4, 1, 2]	2
# [1, 2, 3, 1, 4]		0

# [1,2,1,3],[1,4,1,2]또는 [1, 2, 1, 3, 1], [4, 1, 2] 으로 잘 나눌수 있으므로 2가지 방법이 있다