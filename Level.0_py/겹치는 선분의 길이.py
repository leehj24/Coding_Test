def solution(lines):
    table = [set([]) for _ in range(200)] # -100~100까지 각 선분들의 등장 count 초기화
    for index, line in enumerate(lines):
        x1, x2 = line
        for x in range(x1, x2):
            table[x + 100].add(index) # 선분에 음수가 들어있을 수도 있으므로 +100

    answer = 0
    for line in table:
        if len(line) > 1:
            answer += 1
    return answer
#두개의 이상의 선분이 겹치는 길이를 return
#lines = [[0, 1], [2, 5], [3, 9]]	result=2
#[2,5]와 [3,9] 겹치는 부분은 [3,5]
#[0,1]와 [2, 5]또는 [3,9]와 겹치는 부분은 0 이므로 5-3=2