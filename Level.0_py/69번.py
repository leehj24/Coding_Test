def solution(numbers, n):
    answer = 0
    idx = 0
    while answer <= n:
        answer += numbers[idx]
        idx += 1
    
    return answer

#answer=[5,6,7,8,9] n=17 result=18
#numbers의 원소를 앞에서부터 하나씩 더하다가 
# 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 한다