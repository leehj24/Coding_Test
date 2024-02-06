def coke(answers):
    answer = [0 for i in range(3)]

    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        ans = answers[i]
        if(man1[i%len(man1)] == ans):
            answer[0] += 1
        if(man2[i%len(man2)] == ans):
            answer[1] += 1
        if(man3[i%len(man3)] == ans):
            answer[2] += 1     
    
    result = []
    for i in range(len(answer)):
        if(answer[i] == max(answer)):
            result.append(i+1)
    
    return sorted(result)

def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]

print(coke([1,3,2,4,2]))

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return
# answers	             result
# [1,2,3,4,5]	 [1]
# [1,3,2,4,2]	 [1,2,3]
                