def solution(order):
    stack=[]
    l = len(order)
    num = 0
    idx = 0
    while idx < l:
        if order[idx] > num:
            num +=1
            stack.append(num)
        elif order[idx] == stack[-1]:
            stack.pop()
            idx += 1
        else:
            return idx
    return idx


##

def solution(order):
    answer = 0

    stack = []
    for idx, num in enumerate(order):
        stack.append(idx+1)

        while stack and stack[-1] == order[answer]:
            stack.pop()
            answer +=1

    return answer


##
def solution(order):
    answer = 0

    stack = []
    for idx, num in enumerate(order):
        stack.append(idx+1)

        while stack and stack[-1] == order[answer]:
            stack.pop()
            answer +=1

    return answer

print(solution([4,3,1,2,5]))

# 기사님이 5개의 상자를 실어야 하며, 기존의 컨테이너 벨트에 4,3,1,2,5번째로 놓인 택배상자 순서인 경우, 
# 우선 첫 번째, 두 번째, 세 번째 상자를 보조 컨테이너 벨트에 보관합니다. 그 후 네 번째 상자를 트럭에 싣고 
# 보조 컨테이너 벨트에서 세 번째 상자 빼서 트럭에싣습니다. 다음으로 첫 번째 상자를 실어야 하지만 보조 컨테이너 벨트에서는 두 번째 상자를,
# 기존의 컨테이너 벨트에는 다섯 번째 상자를 꺼낼 수 있기 때문에 더이상의 상자는 실을 수 없습니다. 따라서 트럭에는 2개의 상자만 실리게 됩니다.

# 택배 기사님이 원하는 상자 순서를 나타내는 정수 배열 order가 주어졌을 때, 영재가 몇 개의 상자를 실을 수 있는지 return 하는 solution 함수를 완성하세요.

