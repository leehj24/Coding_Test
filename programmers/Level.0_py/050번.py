def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        l = i%q
        if l ==r:
            answer +=code[i]
    return answer
#code 문자열 index값을 q로 나눈 값이 r인 것만 추출
#code = "qjnwezgrpirldywt" ; q=3 ; r=1 ;result='jerry'