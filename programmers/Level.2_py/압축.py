def solution(msg):
    answer = []
    # 사전 초기화 A~Z
    dic = {chr(i + 64): i for i in range(1, 27)}

    w = c = 0 # 인덱스 초기화
    while True:
        c += 1	
        if c == len(msg):	
            answer.append((dic[msg[w:c]]))
            break
        
        # 만약 [현재글자+다음글자]가 사전에 없다면
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1 # 사전에 추가
            answer.append(dic[msg[w:c]])
            w = c	# 현재글자를 다음글자로 옮겨줌
            
        # 만약 [현재글자+다음글자]가 사전에 있다면 w의 값은 변하지 않고 c의 값만 1씩 증가한다. 
    return answer

## 다른 사람 풀이
def solution(msg):
    a = []
    msg += '_'
    s = list('_ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    while len(msg) > 1:
        i = 0
        while msg[:-i] not in s:
            i += 1
        a += [s.index(msg[:-i])]
        s += [msg[:-i+1]]
        msg = msg[-i:]
    return a

# msg	                    answer
# KAKAO	                    [11, 1, 27, 15]
# TOBEORNOTTOBEORTOBEORNOT	[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# ABABABABABABABAB	        [1, 2, 27, 29, 28, 31, 30]

# 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
# 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
# w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
# 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.

# 현재 사전에는 KAKAO의 첫 글자 K는 등록되어 있으나, 두 번째 글자까지인 KA는 없으므로, 첫 글자 K에 해당하는 색인 번호 11을 출력하고, 다음 글자인 A를 포함한 KA를 사전에 27 번째로 등록한다.
# 두 번째 글자 A는 사전에 있으나, 세 번째 글자까지인 AK는 사전에 없으므로, A의 색인 번호 1을 출력하고, AK를 사전에 28 번째로 등록한다.
# 세 번째 글자에서 시작하는 KA가 사전에 있으므로, KA에 해당하는 색인 번호 27을 출력하고, 다음 글자 O를 포함한 KAO를 29 번째로 등록한다.
# 마지막으로 처리되지 않은 글자 O에 해당하는 색인 번호 15를 출력한다.