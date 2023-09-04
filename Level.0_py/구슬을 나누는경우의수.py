def solution(balls, share):
    a, b = 1, 1
    for i in range(1,share+1):
        a *= balls
        balls -= 1
        b *= i
    return int(a / b)
#또는
import math
def solution(balls, share):
    return math.comb(balls, share)

#서로 다른 구슬 balls개수 중 share만큼 고르는 경우의 수를 return
#서로 다른 구슬 3개 중 2개를 고르는 경우의 수는 3입니다. //3C2=3*2*1/2*1