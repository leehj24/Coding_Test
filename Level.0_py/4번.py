str = input()
for i in str:
    if i.isupper():
        i = i.lower()#소문자로 변경
    else:
        i = i.upper()#대분자로 변경
    print(i, end='')
    #대문자 소문자 바꾸는 것