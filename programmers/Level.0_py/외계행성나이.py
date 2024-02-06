def solution(age):
    str_age = str(age)
    answer = ''
    lst =["a","b","c","d","e","f","g","h","i","j"]
    for ch in str_age:
        for i in range(0,10):
            if int(ch) == i:
                answer += lst[i]
    return answer
#또는
def solution(age):
    conv = {'0':'a','1':'b','2':'c','3':'d','4':'e'
            ,'5':'f','6':'g','7':'h','8':'i','9':'j'}
    return ''.join(conv[i] for i in str(age))

#외계행성이 나이를 알파벳으로 말한다 a=0 b=1...j=9로 답변할때 주어진 age를 외계행성답변처럼 변환후 return
# age=23, result="cd"