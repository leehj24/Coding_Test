def coke(N,stages):
    People = len(stages)
    faillist = {}
    for i in range(1, N + 1):
        if People != 0:
            faillist[i] = stages.count(i) / People
            People -= stages.count(i)
        else:
            faillist[i] = 0

    return sorted(faillist, key=lambda i: faillist[i], reverse=True)

print(coke(5,[2, 1, 2, 6, 2, 4, 3, 3]))

##
def solution(N, stages):
    answer = []
    failure_rates = []  # 실패율 정보를 저장할 리스트
    total_players = len(stages)  # 전체 사용자 수

    for stage in range(1, N + 1):  # 1번 스테이지부터 N번 스테이지까지
        # 해당 스테이지에 도달한 사용자 수
        players_at_stage = stages.count(stage)
        
        if total_players > 0:
            # 실패율 계산
            failure_rate = players_at_stage / total_players
        else:
            # 도달한 사용자가 없는 경우 실패율은 0
            failure_rate = 0
        
        # 실패율 정보 저장 (스테이지 번호와 함께 저장)
        failure_rates.append((stage, failure_rate))
        
        # 아직 남아있는 사용자 수 갱신
        total_players -= players_at_stage

    # 실패율을 기준으로 내림차순 정렬, 실패율이 같으면 스테이지 번호 기준 오름차순
    failure_rates.sort(key=lambda x: (-x[1], x[0]))

    # 정렬된 스테이지 번호만 추출
    answer = [stage[0] for stage in failure_rates]

    return answer

# 테스트 실행
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

# 실패율은 다음과 같이 정의한다다
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
#실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

## stages=[1,2,2,2,,3,5,6]
# 실패율=1->1/8, 2-> 3/7, 3->1/3(8-1(1의 개수)-3(2의 개수))

#N	stages	result
#5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
#4	[4,4,4,4,4]	[4,1,2,3]