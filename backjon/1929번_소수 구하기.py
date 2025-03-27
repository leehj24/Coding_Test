n = list(map(int, input().split()))
for i in range(n[0], n[1] + 1):
    if i < 2:  # 1은 소수가 아님
        continue
    is_prime = True
    for j in range(2, int(i**0.5) + 1):  # i의 제곱근까지만 확인
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
