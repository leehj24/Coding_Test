def sol(word):
    dic ={"A":1, "E":2, "I":3, "O":4, "U":5 }
    n = len(word)
    for i in range(n):
        temp = 0
        for j in range(4-i,-1,-1):
            temp +=5**j
            print(j,temp)
        n += temp *(dic[word[i]]-1)
    return n
        
print(sol("AAAAE"))

from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    words.sort()
    return words.index(word) + 1


def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer


# 자연수n을 k진수로 변환한 수 숫자 0인 기준으로 수를 나누어 소수인 수의 개수를 return
# word	result
# "AAAAE"	6
# "AAAE"	10
# "I"	1563
# "EIO"	1189