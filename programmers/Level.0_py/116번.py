def solution(order):
    answer=0
    for i in order:
        if "latte" in i: 
            answer+=5000
        else: 
            answer+=4500
    return answer
#음료 온도와 상관없이 라떼는 5000 원 아메리카노는 4500원
#order =["americanoice","americano","iceamericano"] result = 13500