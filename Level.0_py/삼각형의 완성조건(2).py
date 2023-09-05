def solution(sides):
    sides.sort()
    L1 = len([i for i in range(1,sides[1]) if i+sides[0]>sides[1]])
    L2 = len([i for i in range(sides[1],sides[0]+sides[1])])
    return L1+L2
#또
def solution(sides):
    return 2 * min(sides) - 1

# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# 삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 나머지 한 변이 될 수 있는 정수의 개수를 return
# sides=[3, 6] result= 5