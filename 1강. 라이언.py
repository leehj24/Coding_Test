#파이썬 터틀을 사용하여 라이언 그리
import turtle           # 터틀 모듈 import

# 화면과 터틀 만들기
s = turtle.Screen()     # 화면(창)은 s에 저장한다.
s.setup(650,800)        # 가로 650, 세로 800 사이즈로 만들기
s.bgcolor("lightcyan")  # 바탕화면 색깔
#s.tracer(0)            # 한번에 업데이트 해서 그린다.
t = turtle.Turtle()     # 터틀을 t에 저장한다.
t.pensize(5)            # 펜 사이즈는 5로 약간 두껍게
t.speed(5)              # 그림 그려지는 속도
t.color("black", "#f0a53a") # 선색깔 검정, 채우기색깔 오렌지같은 라이언색깔

#def makelion():
# 라이언 몸 그리기 
t.penup()       # 그리지 않고 위치만 이동하기 위해서 펜 up(들기)
t.goto(-90, 20) # 왼쪽 어깨로 이동
t.pendown()     # 그리기 위해서 펜 down(찍기)
t.begin_fill()  # 이제부터 그리는 영역은 채우기 시작 (end_fill을 만날때 채우기)
t.setheading(220)   # 터틀(화살표) 이동방향 바꾸기
t.circle(80, 100)   # 왼팔은 원으로 그리는데, 360도 다 그리지 않고 100도만 그린다.
t.setheading(270)   # 아래쪽으로 방향 270도 돌리기
t.forward(100)      # 왼쪽 다리 (100 이동)
t.circle(35, 180)   # 왼발은 원으로 그리는데, 360도 다 그리지 않고 180도만 그린다.(반원)
t.forward(20)       # 앞으로 20 이동
t.right(90)         # 오른쪽으로 방향 90도 돌리기
t.forward(40)       # 앞으로 40 이동
t.right(90)         # 오른쪽으로 방향 90도 돌리기
t.forward(20)       # 앞으로 20 이동
t.circle(35, 180)   # 오른발은 원으로 그리는데, 360도 다 그리지 않고 180도만 그린다.(반원)
t.forward(100)      # 앞으로 100 이동
t.setheading(40)    # 방향 40도 돌리기
t.circle(80, 100)   # 오른팔은 원으로 그리는데, 360도 다 그리지 않고 100도만 그린다.
t.goto(-90, 20)     # 시작점으로 이동 (왼쪽 어깨)
t.end_fill()        # 영역 색깔 채우기
    
# 팔, 몸 구분해주기
# 왼팔 구분
t.penup()           # 그리지 않고 위치만 이동하기 위해서 펜 up(들기)
t.goto(-90, -30)    # 좌표로 이동
t.pendown()         # 그리기 위해서 펜 down(찍기)
t.goto(-90, -100)   # 좌표로 이동
# 오른팔 구분
t.penup()           # 펜 들기
t.goto(90, -30)     # 오른팔 구분
t.pendown()         # 펜 다운
t.goto(90, -100)    # 좌표로 이동   

# 가슴 무늬 그리기
t.color("white", "white")   # 선색, 채우기색 모두 흰색으로
t.penup()           # 펜 들기
t.goto(40, -40)     # 좌표로 이동
t.pendown()         # 펜 다운
t.begin_fill()      # 이제부터 그리는 영역은 채우기 시작 (end_fill을 만날때 채우기)
t.goto(20, -60)     # 좌표로 이동
t.goto(0, -40)      # 좌표로 이동
t.goto(-20, -60)    # 좌표로 이동
t.goto(-40, -40)    # 좌표로 이동
t.setheading(240)   # 터틀(화살표) 이동방향 240도 바꾸기
t.circle(47, 240)   # 원을 그리는데, 360도 다 그리지 않고 240도만 그린다.
t.end_fill()        # 영역 색깔 채우기

# 귀 그리기
t.color("black", "#f0a53a") # 선색깔 검정, 채우기색깔 오렌지같은 라이언색깔
# 왼쪽 귀
t.penup()           # 펜 들기
t.goto(-70, 210)    # 좌표로 이동
t.pendown()         # 펜 다운
t.begin_fill()      # 이제부터 그리는 영역은 채우기 시작 (end_fill을 만날때 채우기)
t.setheading(120)   # 터틀(화살표) 이동방향 120도 바꾸기
t.circle(30, 210)   # 원을 그리는데, 360도 다 그리지 않고 210도만 그린다.
t.end_fill()        # 영역 색깔 채우기
# 오른쪽 귀
t.penup()           # 펜 들기
t.goto(70, 210)     # 좌표로 이동
t.pendown()         # 펜 다운
t.begin_fill()      # 이제부터 그리는 영역은 채우기 시작 (end_fill을 만날때 채우기)
t.setheading(60)    # 터틀(화살표) 이동방향 120도 바꾸기
t.circle(-30, 210)  # 원을 그리는데, 360도 다 그리지 않고 210도만 그린다. 
t.end_fill()        # 영역 색깔 채우기

# 얼굴 그리기
t.penup()           # 펜 들기
t.goto(0, 230)      # 좌표로 이동
t.pendown()         # 펜 다운
t.begin_fill()      # 이제부터 그리는 영역은 채우기 시작 (end_fill을 만날때 채우기)
t.setheading(180)   # 터틀(화살표) 이동방향 180도 바꾸기
t.circle(130)       # 원을 그린다.
t.end_fill()        # 영역 색깔 채우기

t.pensize(10)       # 펜 사이즈 다시 5로
# 왼쪽 눈썹
t.penup()           # 펜 들기
t.goto(-80, 130)    # 좌표로 이동
t.pendown()         # 펜 다운
t.goto(-30, 130)    # 좌표로 이동
# 오른쪽 눈썹
t.penup()           # 펜 들기
t.goto(80, 130)     # 좌표로 이동
t.pendown()         # 펜 다운
t.goto(30, 130)     # 좌표로 이동

# 왼쪽 눈
t.penup()           # 펜 들기
t.goto(-55, 110)    # 좌표로 이동
t.pendown()         # 펜 다운
t.dot(15)           # 현재 좌표를 중심으로 점을 찍는다.
# 오른쪽 눈
t.penup()           # 펜 들기
t.goto(55, 110)     # 좌료로 이동
t.pendown()         # 펜 다운
t.dot(15)           # 현재 좌표를 중심으로 점을 찍는다.

# 코 그리기
t.pensize(5)
t.color("black", "white")
t.penup()               # 펜 들기
t.goto(-10, 80)         # 좌표로 이동
t.pendown()             # 펜 다운
t.begin_fill()          # 이제부터 그리는 영역은 채우기 시작 (end_fill을 만날때 채우기)
t.setheading(155)       # 터틀(화살표) 이동방향 155도 바꾸기
t.circle(18, 240)       # 왼쪽
t.circle(25, 25)
t.right(116)            # 오른쪽으로 방향 116도 돌리기
t.circle(25, 25)        # 오른쪽
t.circle(18, 240)
t.goto(0, 80)           # 좌표로 이동
t.dot(20)               # 까만코 점 그리기
t.end_fill()            # 영역 색깔 채우기
           
#s.ontimer(makelion, 15000)
t.hideturtle()          # 터틀 모양(화살표) 보이지 않게 숨기기
s.update()              # 화면 업데이트
s.mainloop()            # 창 닫히지 않도록 한다.

