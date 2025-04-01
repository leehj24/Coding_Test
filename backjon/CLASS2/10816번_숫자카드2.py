from collections import Counter

n = int(input())
n_card = list(map(int, input().split()))
m = int(input())
m_card = list(map(int, input().split()))

n_count = Counter(n_card)
result = [n_count[num] for num in m_card]

print(' '.join(map(str, result)))
