# from intertools import combinations as c

def solution(number):
    num = c(number,3)
    tri = [n for n in num if not sum(n)]
    return len(tri)

def solution(number):
    answer=0
    l = len(number)
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer

#  3명의 정수 번호를 더했을 때 0이 될 수 있는 방법의 수를 반환하세요.
# number               result
# [-2, 3, 0, 2, -5,7]     3

