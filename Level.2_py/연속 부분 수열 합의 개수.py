def coke(elements):
    result = set()
    
    elementLen = len(elements)
    # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
    elements = elements * 2
    
    for i in range(elementLen):
        for j in range(elementLen):
            result.add(sum(elements[j:j+i+1]))
    return len(result)

print(coke([7,9,1,1,4]))

#원형수열인 [7,9,1,1,4]를 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return

# 길이가 1인 연속 부분 수열로부터 [1, 4, 7, 9] 네 가지의 합이 나올 수 있습니다.
# 길이가 2인 연속 부분 수열로부터 [2, 5, 10, 11, 16] 다섯 가지의 합이 나올 수 있습니다.
# 길이가 3인 연속 부분 수열로부터 [6, 11, 12, 17, 20] 다섯 가지의 합이 나올 수 있습니다.
# 길이가 4인 연속 부분 수열로부터 [13, 15, 18, 21] 네 가지의 합이 나올 수 있습니다.
# 길이가 5인 연속 부분 수열로부터 [22] 한 가지의 합이 나올 수 있습니다.
# 이들 중 중복되는 값을 제외하면 다음과 같은 18가지의 수들을 얻습니다