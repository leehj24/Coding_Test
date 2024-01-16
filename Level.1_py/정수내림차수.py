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


def solution(price, money, count):
    sum = 0
    for i in range(1,count+1): 
        sum += price*i 
       
    money -= sum 

    if money>0: 
        return 0
    else:
        return abs(money) 
    
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)


def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))

# 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록
#rice	money	count	result
# 3	    20	    4	    10