# <입력:60 2 3 , 55 10 5> <출력: 1,0>
def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1

    return 0