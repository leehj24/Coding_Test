def coke(number,limit,power):
    answer = 0
    
    result = [1] * number
    for i in range(2, number + 1):
        li = list()
        for j in range(1, int(i ** 0.5) + 1):
            if (i % j == 0):
                li.append(j)
                li.append(i // j)
        
        if (len(set(li)) > limit):
            result[i - 1] = power
        else:
            result[i - 1] = len(set(li))
    answer = sum(result)
    return answer


def solution(number, limit, power):
    answer = 0 
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 1
                if i // j != j:
                    count += 1

            if count > limit:
                break

        if count > limit:
            answer += power
        else:
            answer += count
    return answer


# 5번으로 지정된 기사단원은 15의 약수가 1, 3, 5 ,15로 4개 이므로, 공격력이 4인 무기를 구매합니다. 만약, 이웃나라와의 협약으로 정해진 공격력의 제한수치가 3이고 
# 초과한 기사가 사용할 무기의 공격력이 2라면, 15번으로 지정된 기사단원은 무기점에서 공격력이 2인 무기를 구매합니다. 
# number	limit	power	result
# 5	        3	    2	    10
# 10	    3	    2	    21