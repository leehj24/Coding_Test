def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c

#또는
def solution(babbling):
    result = 0
    for i in babbling:
        cnt = 0
        word = ''
        for j in i:
            word += j
            if word in ['aya', 'ye', 'woo', 'ma']:
                word = ''
                cnt += 1
        if len(word) == 0 and cnt > 0:
                result += 1
    return result

#문자열 배열에 "aya", "ye", "woo", "ma"기 들어간 단어의 개수를 return
#babbling =["ayaye", uuuma","ye","yemawoo","ayaa"]	result=3

