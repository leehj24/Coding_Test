from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)
#또는
def solution(numbers, direction):
    answer = []
    if direction=="right":
        return numbers[-1:]+numbers[:-1]
    else:
        return numbers[1:]+numbers[:1]
# numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return
# numbers=[1,2,3] direction="right" result=[3,1,2]