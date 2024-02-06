def coke(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

print(coke(3))


def solution(n):
    answer = []
    for i in range(n+1):
        if i==0 or i==1:
            answer.append(i)
        else:
            f = answer[i-1] + answer[i-2]
            answer.append(f % 1234567)

    return answer[-1]

# 피보나치수를 다음과 같은 규칙일때 
# n번째 피보나치수를 1234567으로 나눈 나머지를 return

# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5