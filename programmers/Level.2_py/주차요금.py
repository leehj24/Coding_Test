def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    car_parking = {}  # 차량 번호별로 입차 시간을 저장할 딕셔너리
    car_time = {}  # 차량 번호별로 누적 주차 시간을 저장할 딕셔너리
    car_set = set()  # 주차장에 있는 차량 번호를 추적할 set

    # 입/출차 기록을 처리
    for record in records:
        time, car_num, action = record.split()
        hour, minute = map(int, time.split(":"))
        total_minutes = hour * 60 + minute  # 시:분을 분 단위로 변환
        
        if action == "IN":
            car_parking[car_num] = total_minutes  # 입차 시간 기록
            car_set.add(car_num)  # 입차한 차량을 추적
        else:  # "OUT"
            in_time = car_parking.pop(car_num)  # 출차한 차량의 입차 시간
            parked_time = total_minutes - in_time  # 주차 시간 계산
            if car_num not in car_time:
                car_time[car_num] = 0  # 초기화가 필요한 경우
            car_time[car_num] += parked_time  # 차량별 누적 주차 시간 추가

    # 주차장에 남아 있는 차량들은 23:59에 출차된 것으로 간주
    for car_num in car_set:
        if car_num in car_parking:  # 23:59에 출차된 것으로 간주
            in_time = car_parking[car_num]
            parked_time = (23 * 60 + 59) - in_time  # 23:59에 출차된 것으로 간주
            if car_num not in car_time:
                car_time[car_num] = 0  # 초기화가 필요한 경우
            car_time[car_num] += parked_time  # 누적 주차 시간 추가

    # 주차 요금을 계산
    result = []
    for car_num in sorted(car_time.keys()):  # 차량 번호 오름차순으로 정렬
        total_time = car_time[car_num]
        
        if total_time <= base_time:
            result.append(base_fee)  # 기본 시간 이하일 경우 기본 요금
        else:
            extra_time = total_time - base_time
            extra_fee = (extra_time + unit_time - 1) // unit_time * unit_fee  # 올림 처리
            result.append(base_fee + extra_fee)  # 기본 요금 + 초과 시간 요금

    return result

# 주차요금 fees = [기본시간, 기본요금, 단위시간, 단위요금] 일때 records에는 입차/출차 기록이 담긴 문자열 배열이 주어집니다.
# 차량 번호는 1부터 10,000까지 자연수이며, 시간은 00:00부터 23:59까지 1분 단위로 표기합니다.
# records의 각 원소는 시간을 기준으로 오름차순으로 정렬되어 주어집니다.
# 이때 records를 기반으로 주차요금을 계산하여 차량별 주차요금을 나타내는 배열을 return 

# 입출력 예

# fees	                records	                                                result
# [180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
#                       "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", 
#                       "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
# [120, 0, 60, 591]	    ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT",
#                       "18:00 0202 OUT","23:58 3961 IN"]	                    [0, 591]
# [1, 461, 1, 10]	    ["00:00 1234 IN"]	                                    [14841]