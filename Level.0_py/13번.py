# <입력: a=82 b=5> <출력:825> <825와 582중에 더 큰것을 출력>
def solution(a, b):
    a, b = str(a), str(b)
    return int(max(a+b, b+a))