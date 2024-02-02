def coke(s):
    stack=[]
    for i in s:
        if i=="(":
            stack.append(i)
        else:   # i==")"
            if stack:   #stack이 있다면
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

def coke(s):
    answer = 0
    for c in s:
        if c == "(":
            answer += 1
        else:
            if answer > 0:
                answer -= 1
            else:
                return False
    if answer > 0:
        return False
    return True
print(coke("()()"))
    
# 문자열 s에서 올바른 괄호()가 있으면 true값을 없음면 false값을 return
# )수만큼 stack에 쌓은 (를 제거, stack이 남으면 flase
# s         result
# "()()"    true
# "(()()"   flase
# ")()("    flase