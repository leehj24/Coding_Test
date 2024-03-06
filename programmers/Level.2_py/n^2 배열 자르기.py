def check(n,left,right):
    answer = []

    for i in range(left, right + 1):
        print(i//n, i&n)
        answer.append(max(i // n, i % n) + 1)

    return answer

print(check(4,7,14))
#배열 1-n까지 다음과 같이 나열한다 하였을때, a[i]행별로 모두 이어붙인다
#새로운 1차원 배열에서 arr[left:right]를 나열하여라

# 1 2 3 4   # 1 2 3 4 5
# 2 2 3 4   # 2 2 3 4 5
# 3 3 3 4   # 3 3 3 4 5
# 4 4 4 4   # 4 4 4 4 5
            # 5 5 5 5 5

# 1234223433344444