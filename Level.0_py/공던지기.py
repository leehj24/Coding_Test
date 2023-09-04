def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]
# numbers=[1,2,3,4,5] k=2 result=1
# numbers에 있는 배열순대로 한명을 건너뛰고 
# 그 다음순으로 공을 던진다 하였을 때 k번째로 공을 던지는 사람의 번호는 무엇인지 return 
