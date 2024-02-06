def solution(sizes):
    m=[]
    n=[]
    for i in sizes:
        m.append(max(i))
        n.append(min(i))
        print(max(i),min(i))
    return max(m)*min(n)

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

#가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어질 때, 모든 명함을 수납할 수 있는 가장 작은 지갑의 크기를 
# sizes                                     result
# [[60, 50], [30, 70], [60, 30], [80, 40]]  2400

