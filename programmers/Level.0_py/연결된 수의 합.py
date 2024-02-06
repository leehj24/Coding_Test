def solution(num, total):
    average = total // num
    return [i for i in range(average - (num-1)//2, average + (num + 2)//2)]

# 연속되는 숫자의 합이 total이 되게끔 return //이때 연속되는 숫자의 갯수는 num 만큼이여야한다.
# num   total     결과
#  3      12   [3,4,5]
#  5      15   [1,2,3,4,5]
#  4      14   [2,3,4,5]
# num이 홀수면 toal//num은 가운데에 있고 쪽수면 가운데의 왼쪽에 있다.