def solution(polynomial):
    coef = 0
    const = 0
    for term in polynomial.split(' + '):
        if 'x' in term:
            if len(term) != 1:
                coef += int(term[:-1]) - 1
            coef += 1 
        else:
            const += int(term)
    answer = []
    if coef != 0:
        answer.append('x' if coef == 1 else f'{coef}x')
    if const != 0:
        answer.append(str(const))
# 또는
def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'
    
#문자열 polynomial에 있는 다항식을 계산하여 return
#polynomial="3x+3+x" result='4x+4'