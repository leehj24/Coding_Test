def coke(n):
    cnt=0
    while n>0:
        if n %2==0:
            n=n//2
        else:
            n=n-1
            cnt +=1
    print(n,cnt)
print(coke(5))

def solution(n):
    return bin(n).count('1') # 이진수 n에서 1의 개수

# k만큼 점프하거나 현재까지 온거리 *2 자리에 순간이동 할수 있는 슈트가 있다.
#거릭 n일때 슈트로 최소 몇번 이동하면 다 도착하는지 return하라
# n	 result
# 5	 2