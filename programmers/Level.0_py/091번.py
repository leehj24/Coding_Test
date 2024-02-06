def solution(myStr):
    myStr = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()
    return myStr if myStr else ["EMPTY"]

#문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 한다
#문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은 ["onlettu", "etom", "to"] 가 된다