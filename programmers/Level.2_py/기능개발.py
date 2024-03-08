def solution(progresses, speeds):

    answer = []
    day = 0         # 작업 일수 (배포 날짜)
    count = 0       # 배포된 작업 개수

  # 100 % 인지 확인하는 식 : progresses(현재 작업진도) + day(걸린 일수) * speeds(작업 속도)

    while len(progresses) > 0 :

        if ( progresses[0] + day * speeds[0] ) >= 100 :     # 작업진도가 100% 이상이면

            progresses.pop(0)                               # 작업진도 리스트와
            speeds.pop(0)                                   # 작업속도 리스트에서 삭제한 후
            count += 1                                      # 배포 개수 1 증가
            #day=7 count=1 // day = 7 count = 2
        else :

            if count > 0 :                                  # 현재는 작업진도가 100% 이상이 아닌데, 앞에서 배포할 작업이 있었다면
                answer.append(count)                        # 배포개수를 answer 리스트에 담아준 후
                count = 0                                   # 초기화

            day += 1                                        # 다음 날짜 작업을 확인하기 위해 작업 일수에 하루를 더해줌

    answer.append(count)                                    # 마지막 배포된 작업들에 대해서 append 를 실행하지 않고 while문을 빠져나왔기 때문에 처리해줘야함

    return answer



print(solution([93, 30, 55],[1, 30, 5]))

# 입출력 예 #1
# 첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
# 두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
# 세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.

# 따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 


#입출력
# progresses	            speeds	            return
# [93, 30, 55]	            [1, 30, 5]	        [2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]