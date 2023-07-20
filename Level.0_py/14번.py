# <입력: a=12, b=3> <출력 123> <123 과 2*12*3 중에 더 큰값 출력>
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)