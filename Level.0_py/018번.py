def solution(ineq, eq, n, m):
    answer = 0
    if n > m and ineq ==">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1

    return answer
#또는 

def solution(ineq, eq, n, m):
    answer = 0
    if (ineq == '>' and eq == '='):
        answer = 1 if n >= m else 0
    elif (ineq == '<' and eq == '='):
        answer = 1 if n <= m else 0
    elif (ineq == '>' and eq == '!'):
        answer = 1 if n > m else 0
    elif (ineq == '<' and eq == '!'):
        answer = 1 if n < m else 0
    
    return answer