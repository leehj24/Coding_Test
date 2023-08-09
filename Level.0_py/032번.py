def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        isAdd = True
        for s in str(num):
            if s not in ["0", "5"]:
                isAdd = False
                break
        if isAdd:
            answer.append(num)
    if len(answer) == 0:
        answer.append(-1)
    return answer
#l=5 r= 100 answer = [5,50,55] l과 r사이에 있는 숫자중에 5와 0만 있는 수 만 출력