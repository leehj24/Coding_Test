def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        if int(i[s:s+l]) > k:
            answer.append(int(i[s:s+l]))
    return answer

# 배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환합니다. 
# 이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return

# intStrs= ["0123456789","9876543210","9999999999999"]
# k=50000 s=5 l=5
# result= [56789, 99999]