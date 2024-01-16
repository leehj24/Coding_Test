def solution(n):
    add=[]
    for i in str(n):
        add.append(i)
    answer = sorted(add,reverse=True)
    return int(''.join(answer))

def solution(n):
    ls = list(str(int(n)))
    ls.sort(reverse = True)
    return int("".join(ls))

# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.


