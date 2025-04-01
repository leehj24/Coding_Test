n = list(map(int, input().split()))
k = [int(input()) for _ in range(n[0])]

Div = max(k)
low, high = 1, Div

while low <= high:
    mid = (low + high) // 2
    div = [i // mid for i in k]
    if sum(div) >= n[1]:
        low = mid + 1
    else:
        high = mid - 1

print(high)


    