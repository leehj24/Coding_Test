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