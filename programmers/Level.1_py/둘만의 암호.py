def coke(s,skip,index):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in skip:
        alpha=alpha.replace(i,"")
    
    answer =""
    for j in s:
        if alpha.find(j)+index<len(alpha):
            answer+=alpha[alpha.find(j)+index]
        else:
            answer+=alpha[alpha.find(j)+index-len(alpha)]
    return answer

print(coke("aukks","wbqd",5))

def solution(s, skip, index):
    answer = ""
    
    alpha = "abcdefghijklmnopqrstuvwxyz" # 알파벳
    
    for j in skip: # ch => skip의 문자 하나하나
        if j in alpha:
            alpha = alpha.replace(j, "") # 알파벳 안에 skip 문자들 제거
    
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)] # s의 문자 인덱스 + index를 alpha의 길이로 나눈 나머지를 알파벳으로 변환
        answer += change
    
    return answer

def solution(s, skip, index):
    answer = ''
    
    for c in s:
        i = ord(c)
        j = index
        while j > 0:
            i += 1
            if i > ord('z'):
                i = ord('a')
            if chr(i) in skip:
                j += 1
            j -= 1
        answer += chr(i)
    
    return answer

# 문자열 alpha에 문자열 skip을 제외한 문자열을 return
#s	        skip	index	result
#"aukks"    "wbqd"  5       "happy"