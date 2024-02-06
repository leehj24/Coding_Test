def solution(a, b):
    answer = 0
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    
    for i in range(a-1):
      answer += months[i]
    
    answer += b-1
    answer = answer%7
    
    return days[answer]

def solution(a, b):
    days = ['THU', 'FRI', 'SAT','SUN', 'MON', 'TUE','WED']
    months = [31,29,31,30,31,30, 31, 31, 30, 31, 30, 31]
    
    return days[(sum(months[:a-1])+b)%7]

# 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요
#a	b	result
#5	24	"TUE"