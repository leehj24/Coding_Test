num = int(input())  # 테스트 케이스 개수 입력
array = []
for _ in range(num):
    value = list(map(int, input().split()))  # 각 테스트 케이스 입력
    array.append(value)

for case in array:
    M, N, x, y = case  # 각각 M, N, x, y를 할당
    year = x  # x를 기준으로 시작
    valid = False

    while year <= M * N:  # 최대 M * N까지만 탐색 (최소공배수)
        # year의 y값이 주어진 y값과 일치하는지 확인
        if (year - 1) % N + 1 == y:
            print(year)  # 결과 출력
            valid = True
            break
        year += M  # M의 주기로 이동

    if not valid:
        print(-1)  # 유효하지 않은 경우 -1 출력
