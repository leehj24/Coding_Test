def solution(n, k):
    return [i for i in range(k,n+1,k)]

#또는
def solution(n, k):
    answer = []
    for i in range(1,n+1):
        if k*i <=n:
            answer.append(k*i)
        else:
            pass
    return answer

#n=10 ,k=3 ,result = [3,6,9]