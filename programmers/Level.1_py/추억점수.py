
def solution(name,yearning,photo):
    answer = []
    for ppl in photo:
        score = 0
        for n in ppl:
            if n in name:
                score += yearning[name.index(n)]
        answer.append(score)
    return answer
def solution(name,yearning,photo):
    return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]

# 배열 array를 이진법으로 하였을 때 0은 공백 1은 #으로 채웠을 경우 배열 2개를 합쳤을 때 둘중 하나라도 #있을시 채워놓는다 하였을 때 배열 합쳤을때의 결과를 return
# name	                               yearning	            photo	                                    result
# [ "may", "kein", "kain", "radi" ]    [ 5, 10, 1, 3 ]      [[ "may", "kein", "kain", "radi" ],         [ 19, 15, 6 ]
#                                                           [ "may", "kein", "brin", "deny" ],
#                                                           [ "kon", "kain", "may", "coni" ]]