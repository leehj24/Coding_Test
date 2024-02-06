from collections import Counter  
def check(want,number,discount):
    answer = 0
    check = {}
    for w, n in zip(want, number):
        check[w] = n
    
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if c == check:
            answer += 1

    return answer

def solution(want, number, discount):
    answer = 0
    list_all_want = []

    for i in range(len(want)):
        for j in range(number[i]):
            list_all_want.append(want[i])
    list_all_want.sort()

    for i in range(len(discount) - 9):
        list_10 = discount[i: i+10]
        list_10.sort()
        if list_all_want == list_10:
            answer += 1

    return answer

print(check(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],
            ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))

#정현이는 원하는 제품want 가 number만큼 필요하다고 했을 때,
# 언제 회원가입 하면 가장 이득인지 회원등록 날짜의 일수를return

# XYZ 마트에서 15일간 회원을 대상으로 할인하는 제품이 날짜 순서대로 치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나인 경우
# 첫째 날부터 열흘 간에는 냄비가 할인하지 않기 때문에 첫째 날에는 회원가입을 하지 않습니다. 
# 둘째 날부터 열흘 간에는 바나나를 원하는 만큼 할인구매할 수 없기 때문에 둘째 날에도 회원가입을 하지 않습니다. 
# 셋째 날, 넷째 날, 다섯째 날부터 각각 열흘은 원하는 제품과 수량이 일치하기 때문에 셋 중 하루에 회원가입을 하려 합니다.