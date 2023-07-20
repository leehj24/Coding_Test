#입출력 반복 a는 문자열 b는 숫자 
# a= strings b= 3 결과: stringstringstring
a, b = input().strip().split(' ')
b = int(b)
print(a*b)