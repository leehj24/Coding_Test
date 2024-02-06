def solution(strings, n):
    new = []
    for i in strings:
        new.append(i[n]+i)
    new.sort()
    answer =[]
    for i in new:
        answer.append(i[1:])
    return answer

def solution(strings, n):
    return sorted(strings,key = lambda x: (x[n], x))

print(solution(["abce", "abcd", "cdx"],2))
#strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"를 오름차순대로 strings를 정렬
# string                    n           result
# ["sun", "bed", "car"]     1	    ["car", "bed", "sun"]
# ["abce", "abcd", "cdx"]	2	    ["abcd", "abce", "cdx"]