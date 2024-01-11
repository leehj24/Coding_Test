def solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer

def solution(chicken):
    answer = 0
    while chicken >= 10:
        div, mod = divmod(chicken, 10)
        answer += div
        chicken = div+mod
    return answer



# 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다. 
# 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return

# chicken	result
# 100	11
# 1,081	120
