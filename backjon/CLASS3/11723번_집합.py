n = int(input())
k = [list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(n)]
s = set()  # 리스트 대신 집합 사용

for i in k:
    if i[0] == "add":
        s.add(i[1])  # 집합에 추가
    elif i[0] == "remove":
        s.discard(i[1])  # 집합에서 제거 (존재하지 않아도 에러 발생하지 않음)
    elif i[0] == "check":
        print(1 if i[1] in s else 0)  # 집합에 포함 여부 확인
    elif i[0] == "toggle":
        if i[1] in s:
            s.remove(i[1])  # 집합에서 제거
        else:
            s.add(i[1])  # 집합에 추가
    elif i[0] == "all":
        s = set(range(1, 21))  # 1부터 20까지의 숫자를 집합으로 설정
    elif i[0] == "empty":
        s.clear()  # 집합 비우기
        
## 위에건 메모리 초과

####
import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

s = set()  # 집합 사용
m = int(input().strip())  # 명령의 개수 입력

for _ in range(m):
    command = input().strip().split()
    
    if command[0] == "add":
        s.add(int(command[1]))  # 집합에 추가
    elif command[0] == "remove":
        s.discard(int(command[1]))  # 집합에서 제거 (존재하지 않아도 에러 발생하지 않음)
    elif command[0] == "check":
        print(1 if int(command[1]) in s else 0)  # 집합에 포함 여부 확인
    elif command[0] == "toggle":
        num = int(command[1])
        if num in s:
            s.remove(num)  # 집합에서 제거
        else:
            s.add(num)  # 집합에 추가
    elif command[0] == "all":
        s = set(range(1, 21))  # 1부터 20까지의 숫자를 집합으로 설정
    elif command[0] == "empty":
        s.clear()  # 집합 비우기