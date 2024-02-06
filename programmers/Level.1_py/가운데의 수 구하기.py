def solution(s):
    if len(s)%2!=0:
        return s[len(s)//2]
    else:
        return s[len(s)//2-1]+s[len(s)//2]

# 문자열 가운데를 추출하여 return
# a          result
#"1,2,3,4,5"    3
#"1,2,3,4"      2,3