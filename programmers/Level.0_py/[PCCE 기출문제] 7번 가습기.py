def func1(humidity, val_set):
    if humidity < val_set:
        return 3
    return 1

def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4
    else:
     return 5

def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 0

def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity)

    elif mode_type == "target":
        answer = func1(humidity, val_set)

    elif mode_type == "minimum":
        answer = func3(humidity, val_set)

    return answer


# "auto" 모드
# 습도가 0 이상 10 미만인 경우 : 5단계
# 습도가 10 이상 20 미만인 경우 : 4단계
# 습도가 20 이상 30 미만인 경우 : 3단계
# 습도가 30 이상 40 미만인 경우 : 2단계
# 습도가 40 이상 50 미만인 경우 : 1단계
# 습도가 50 이상인 경우 : 0단계

# "target" 모드
# 습도가 설정값 미만일 경우 : 3단계
# 습도가 설정값 이상일 경우 : 1단계

# "minimum"모드
# 습도가 설정값 미만일 경우 : 1단계
# 습도가 설정값 이상일 경우 : 0단계

# mode_type	humidity	val_set	result
# "auto"	23	45	3
# "target"	41	40	1
# "minimum"	10	34	1

# 입출력 예 #1

# "auto"모드이므로 습도에 따라 가습량이 조절됩니다. 현재 습도가 20 이상 30 미만이므로 3을 return합니다.
# 입출력 예 #2

# "target"모드이고, 설정값보다 습도가 높으므로 1을 return합니다.
# 입출력 예 #3

# "minimum"모드이고, 설정값보다 습도가 낮으므로 1을 return합니다.