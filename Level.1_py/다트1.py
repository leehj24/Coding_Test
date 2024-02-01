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
#옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상() 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# dart      result      예시
# 1S2D*3T	37	        1^1 * 2 + 2^2 * 2 + 3^3   

