def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]

#배열에서 두개를 곱해 최대값을 만들어라
#numvers=[0, 31, 24, 10, 1, 9]	result=744 