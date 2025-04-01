n = list(map(int, input().split()))
k= [input() for _ in range(n[0])]
find =[]

for _ in range(n[1]):
    value = input().strip()  # 입력값을 공백 제거 후 처리
    if value.isdigit():  # 숫자인 경우
        find.append(int(value))  # 정수로 변환
    else:  # 문자인 경우
        find.append(value)

for i in range(len(find)):
    if isinstance(find[i], str) and find[i] in k:  # 문자열이면서 k에 있는 경우
        print(k.index(find[i]) + 1)  # 인덱스는 1부터 시작
    elif isinstance(find[i], int) and 1 <= find[i] <= len(k):  # 숫자인 경우
        print(k[find[i] - 1])  # k 리스트의 해당 번호 출력
    else:  # 유효하지 않은 입력 처리 (필요시 추가)
        print("잘못된 입력입니다.")
    
 ## 위에껀 시간초과 나옴....핳
import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

n, m = map(int, input().split())  # n: 포켓몬 개수, m: 문제 개수
k = [input().strip() for _ in range(n)]  # 포켓몬 이름 리스트

# 딕셔너리 생성
pokemon_to_number = {k[i]: i + 1 for i in range(n)}  # 이름 -> 번호
number_to_pokemon = {i + 1: k[i] for i in range(n)}  # 번호 -> 이름

# 문제 처리
for _ in range(m):
    query = input().strip()
    if query.isdigit():  # 숫자인 경우
        print(number_to_pokemon[int(query)])
    else:  # 문자열인 경우
        print(pokemon_to_number[query])