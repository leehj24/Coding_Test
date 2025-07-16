n = int(input())

people =[]

for _ in range(n):
    wieght , height = map(int,input().split())
    people.append([wieght,height])

for i in range(n):
    rank =1
    for j in range(n):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    print(rank, end=' ')



"""
각 사람은 (몸무게, 키)로 덩치를 표현함.

두 조건 모두 더 크면 덩치가 더 큰 것으로 간주함.

한 사람의 덩치 등수는, 자신보다 덩치가 더 큰 사람이 몇 명인지 세고 그 수 + 1임.

모든 사람의 덩치 등수를 계산해서 순서대로 출력함.

📥 입력 형식
첫 줄: 사람 수 N (2 ≤ N ≤ 50)

다음 N줄: 각 사람의 몸무게 키 정보

📤 출력 형식
각 사람의 덩치 등수를 공백으로 구분해 한 줄에 출력


"""