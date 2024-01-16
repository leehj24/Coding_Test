def solution(n):
    answer =""
    if len(n)%2!=0:
        answer +="수"
    else:
        answer +="박"

def solution(n):
    return ('수박'*n) [:n]

# 길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수
# n     result
# 3	    "수박수"
# 4     "수박수박"