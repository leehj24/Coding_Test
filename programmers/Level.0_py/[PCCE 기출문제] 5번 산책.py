def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1

        elif i == "S" :
            north -=1

        elif i == "E" :
            east -=1

        elif i == "W" :
            east -=1

    return [east, north]

# N,S,E,W(북,남동,서)가 각자 1만큼 간다고 한다. 기준을 동,북으로 하여 서,남인 경우는 동북에서 음수만큼 떨어진것으로 표현한다.
# 문자열 route라고 하였을때 북,동 기준으로 계한하여 return
# route			result
# "NSSNEWWN"	[-1, 1]
# "EESEEWNWSNWWNS"	[0, 0]

