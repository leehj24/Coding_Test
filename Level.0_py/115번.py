def solution(date1, date2):
    return int(date1 < date2)
#또는 
def solution(date1, date2):
    for i in range(3):
        if date1[i]<date2[i]:return 1
        elif date2[i]<date1[i]: return 0
    return 0

# date1날짜가 date2 날짜보다 앞서면 1, 아니면 0으로 return
# date1[2021, 12, 28]	date2[2021, 12, 29]	result=1