def check(s):
    stack=[]
    for i in s:
        if len(stack)==0:
            stack.append(i)
        else:
            if i==")" and stack[-1]=="(":
                stack.pop()
            elif i=="]" and stack[-1]=="[":
                stack.pop()
            elif i=="}" and stack[-1]=="{":
                stack.pop()
            else:  
                stack.append(i)

    if len(stack)== 0:
        return 1
    else:
        return 0
           
def coke(s):
    cnt = 0
    for i in range(len(s)):
        if check(s):
            cnt +=1
        s= s[1:]+s[:1]
    return cnt

print(coke("[](){}"))
#문자열 s를 왼쪽으로 x만큼 회전시킬때 s가 올바를 괄호 문자열이 되게하는 x의 개수를 return 

from collections import deque

def check(s):
    while True:
        if "()" in s: s=s.replace("()","")
        elif "{}" in s: s=s.replace("{}","")
        elif "[]" in s: s=s.replace("[]","")
        else: return False if s else True       

def solution(s):
    ans = 0
    que = deque(s)

    for i in range(len(s)):
        if check(''.join(que)): ans+=1
        que.rotate(-1)
    return ans

def solution(s):
    count = 0
    i = 0
    for i in range(len(s)):
        stack = []
        for j in s:
            if not stack:
                stack.append(j)
                continue
            if stack[-1] == '[' and j == ']':
                stack.pop()
            elif stack[-1] == '{' and j == '}':
                stack.pop()
            elif stack[-1] == '(' and j == ')':
                stack.pop()
            else:
                stack.append(j)
        s = s[1:] + s[0]
        if not stack:
            count += 1
    return count
