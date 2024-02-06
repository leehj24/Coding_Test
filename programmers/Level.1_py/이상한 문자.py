def solution(s):
    res=""
    ans = []
    for w in s.split(' ') : #단어 순회
        for i in range(len(w)): # 글자 순회
            if i % 2 == 0 : # 인덱스가 짝수
                res+=w[i].upper() #대문자로
            else : 
                res += w[i].lower()
        ans.append(res) #바뀐 단어 넣기
        res = "" #단어 초기화
    return ' '.join(ans) #공백 넣어 출력
            
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
# 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수
# s             result
# hi my name    Hi My NaMe