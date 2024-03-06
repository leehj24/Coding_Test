def check(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1

def solution(clothes):
    hash_map = {}
    for clothe, type in clothes:
    	#옷 종류의 가짓 수 저장, 이전에 값이 있었으면 기존 값에 +1
        hash_map[type] = hash_map.get(type, 0) + 1
    answer = 1
    for type in hash_map:
    	#모든 옷 종유에 대해서 안 입는 경우도 있기 때문에 +1을 해줌
        answer *= (hash_map[type] + 1)
    
    return answer - 1 #아무것도 입지 않은 경우 1를 제외 시켜줌

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

print(check([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

# 코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다.
# 코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

# clothes	return
# [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
# [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	3


# 1. yellow_hat
# 2. blue_sunglasses
# 3. green_turban
# 4. yellow_hat + blue_sunglasses
# 5. green_turban + blue_sunglasses

# headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.