def coke(dart):
    scores = []
    cnt = 0
    bonus = {'S' : 1, 'D' : 2, 'T' : 3 }

    for i in range(len(dart)):
        op = dart[i]
        if op in bonus:
            scores.append(int(dart[cnt:i]) ** bonus[op])
        elif op == '*':
            scores[-2:] = [x * 2 for x in scores[-2:]]
        elif op == '#':
            scores[-1] = -scores[-1]

        if not op.isnumeric():
            cnt = i + 1

    return sum(scores)

def coke(dart):
    num = []  #정제되지 않은 점수 값을 임시로 저장
    score = []  #3번의 시도에 대해 보너스와 옵션이 계산되고나면 시도마다 score 값 저장
    bonus = {'S':1, 'D':2, 'T':3}
#옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상() 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# dart      result      예시
# 1S2D*3T	37	        1^1 * 2 + 2^2 * 2 + 3^3    
    for i in dart:
        if i.isdigit():
            num.append(i)
        elif i in 'SDT':
                score.append(int(''.join(num[0:])) ** bonus[i])   # 점수가 10인 경우도 고려해서 join
                num = []
        elif i == '*':
            if len(score) > 1:
                score[-2] *= 2 
            score[-1] *= 2
        elif i == '#':
            score[-1] *= -1  

    return sum(score)


#점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.


def coke(lottos,win_ums):
    grade={1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    m_in=0 ; m_ax=0
    
    for i in lottos:
        if i in win_ums:
            m_in+=1
    
    for j in lottos:
        print(j)
        if j in win_ums:
            print(m_ax,j)
            m_ax+=1
        elif j ==0:
            print(m_ax,j)
            m_ax+=1

    if m_in == 0:
        m_in = 1
    array=[grade[m_ax],grade[m_in]]
    return array

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

print(coke([31,3,4,5,7,0],[31, 10, 45, 1, 6, 19]))
#새로산 lottos배열에서 모르는 수는 0이며 발표난 로또win_nums 이라 하였을때 0의 수에 따라 최고순위와 최저순위를 return
# 1등-6개일치, 2등-5개일치, 3등-4개일치, 4등-3개일치, 5등-2개일치, 6등 낙첨
#lottos	                win_nums	                result
#[44, 1, 0, 0, 31, 25]  [31, 10, 45, 1, 6, 19]	    [3, 5]
#[0, 0, 0, 0, 0, 0]	    [38, 19, 20, 40, 15, 25]	[1, 6]

