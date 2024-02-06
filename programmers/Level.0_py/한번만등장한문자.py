def solution(s):
    answer = ''
    for i in s:
        if s.count(i)==1:
            answer += i
    print(answer)
    return ''.join(sorted(answer))
#s="hello", result= "eho"
#s문자열에 있는 문자에서 한번만 나오는 것을 오름차순으로 return