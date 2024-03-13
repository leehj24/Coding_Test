def solution(numbers, hand):
    answer = ''
    
    # 키패드 좌표료 변경
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    # 시작 위치
    left_s = dic['*']
    right_s = dic['#']
    
    for i in numbers:
        now = dic[i]
        # 1, 4, 7을 누르는 경우 무조건 왼손
        if i in [1, 4, 7]:
            answer += 'L'
            left_s = now
            
        # 3, 6, 9를 누르는 경우 무조건 오른손
        elif i in [3, 6, 9]:
            answer += 'R'
            right_s = now
            
        # 2, 5, 8, 0을 누르는 경우
        else:
            left_d = 0
            right_d = 0
            
            # 좌표 거리 계산해주기
            for a, b, c in zip(left_s, right_s, now):
                left_d += abs(a-c)
                right_d += abs(b-c)
            
            # 왼손이 더 가까운 경우
            if left_d < right_d:
                answer += 'L'
                left_s = now
                
            # 오른손이 더 가까운 경우
            elif left_d > right_d:
                answer += 'R'
                right_s = now
            
            # 두 거리가 같은 경우
            else:
                # 왼손잡이 경우
                if hand == 'left':
                    answer += 'L'
                    left_s = now
                    
                # 오른손잡이 경우
                else:
                    answer += 'R'
                    right_s = now
            
    return answer

# 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
# 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
# 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.


# numbers 	                        hand	    result
# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"