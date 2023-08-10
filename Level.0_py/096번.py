def solution(arr):
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)
#2의 제곱수의 길이만큼 arr뒤에 정수 0 추가
#arr[1, 2, 3, 4, 5, 6]	result=[1, 2, 3, 4, 5, 6, 0, 0]