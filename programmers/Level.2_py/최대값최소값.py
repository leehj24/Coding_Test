def solution(s):
    answer = [] # 칠하는 횟수
    num = s.split()
    for i in num:
        answer.append(int(i))
    pk=(str(min(answer))+" " +str(max(answer)))
    return pk

def solution(s):
    il = sorted([int(c) for c in s.split(' ')])
    answer = ' '.join([str(il[0]), str(il[len(il)-1])])
    return answer

def solution(s):
    s_list=s.split(" ")
    n = [int(i) for i in s_list]
    n.sort()

    return str(n[0]) + " " + str(n[len(n)-1])

def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

#문자열 s에서 최대값 최소값
#s	            return
#"1 2 3 4"	    "1 4"
#"-1 -2 -3 -4"	"-4 -1"
#"-1 -1"	    "-1 -1"