def solution(s):
    en=['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = ''
    for idx,num in enumerate(en):
        if num in s:
            s=s.replace(num,str(idx))
        answer=s
    return int(answer)
#문자열s에 있는 숫자와 영어를 모두 수로 변환후  return
# s               result
# onetwo34five     12345
