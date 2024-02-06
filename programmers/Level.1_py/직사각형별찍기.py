a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print('*'*a)


a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)

#가로의 길이가 n, 세로의 길이가 m인 직사각형을 *형태를 출력해보세요.

# n m result
# 5 3 *****
#     *****
#     *****