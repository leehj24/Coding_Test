def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]
    
def solution(n, t, m, p):
    answer = ''
    test = ''
    
    for i in range(m*t):
        test += str(convert(i, n))
        
    while len(answer) < t:
        answer += test[p-1]
        p += m
        
    return answer


##
def solution(n, t, m, p):
    m_chars = '0123456789ABCDEF'

    def _rep(numb, to):
        j, k = divmod(numb, to)
        i = m_chars[k]
        return ('' if j == 0 else _rep(j, to)) + i

    numbers = ''
    for i in range(0, t * m):
        numbers += _rep(i, n)
        if len(numbers) >= t * m:
            break

    result = ''
    for i in range(p - 1, t * m, m):
        result += numbers[i]

    return result
    
print(solution(2,4,2,1))

# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.
# n	    t	m	p	result
# 2	    4	2	1	"0111"
# 16	16	2	1	"02468ACE11111111"
# 16	16	2	2	"13579BDF01234567"

#숫자를 0부터 시작해서 차례대로 말한다. 첫 번째 사람은 0, 두 번째 사람은 1, … 열 번째 사람은 9를 말한다.
# 10 이상의 숫자부터는 한 자리씩 끊어서 말한다. 즉 열한 번째 사람은 10의 첫 자리인 1, 열두 번째 사람은 둘째 자리인 0을 말한다.
# 이렇게 게임을 진행할 경우,
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4, …
# 순으로 숫자를 말하면 된다.

# 한편 코딩 동아리 일원들은 컴퓨터를 다루는 사람답게 이진수로 이 게임을 진행하기도 하는데, 이 경우에는
# 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, …
# 순으로 숫자를 말하면 된다.