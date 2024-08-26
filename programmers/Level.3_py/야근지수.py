import heapq

def solution(n, works):
    if n >= sum(works):
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
    
    return sum([w ** 2 for w in works])


#
def noOvertime(n, works):
  if n>=sum(works):
    return 0

  while n > 0:
    works[works.index(max(works))] -= 1
    n -= 1

  result = sum([w ** 2 for w in works])

  return result

# Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.
# Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때, 퇴근까지 남은 N 시간과 
# 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성

# works	    n	result
# [4, 3, 3]	4	12
# [2, 1, 2]	1	6
# [1,1]	    3	0

# 입출력 예 #1
# n=4 일 때, 남은 일의 작업량이 [4, 3, 3] 이라면 야근 지수를 최소화하기 위해 
# 4시간동안 일을 한 결과는 [2, 2, 2]입니다. 이 때 야근 지수는 2^2 + 2^2 + 2^2 = 12 입니다.

