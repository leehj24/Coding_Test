# 파이썬 터틀을 사용하여 라이언 그리기
import turtle

# 색깔 정하기
bg_color = "lightcyan"
line_color = "black"
body_color = "#f0a53a"    #"#edaa4e"   #"orange"
nose_color = "white"
chest_color = "white"

s = turtle.Screen()
s.setup(650, 800)
s.bgcolor(bg_color)
t = turtle.Turtle()
t.pensize(5)
t.speed(3)
print(s.tracer())
#s.tracer(0)

# 몸 그리기
# 좌표순서 왼쪽위(x,y), 왼쪽아래(x,y), 오른쪽아래(x,y), 오른쪽위(x,y)
posbody = [(-90,20),(-90,-150),(90,-150),(90,20),   # 검정(0)
           (-85,20),(-85,-145),(85,-145),(85,20)]   # 주황(1)  
def drawbody(col):
    if col == 0:      # 검정색
        t.color(line_color, line_color)
    elif col == 1:    # 주황색 안쪽
        t.color(body_color, body_color)
    t.penup()
    t.goto(posbody[col*4+0])     
    t.pendown()
    t.begin_fill()
    t.goto(posbody[col*4+1])      
    t.goto(posbody[col*4+2])       
    t.goto(posbody[col*4+3])      
    t.end_fill()

# 다리 그리기
# 좌표순서 왼쪽위(x,y), 왼쪽아래(x,y), 오른쪽아래(x,y), 오른쪽위(x,y)
posleg = [(-90,-140),(-90,-170),(-20,-170),(-20,-140),  # 검정  왼쪽(0,0)
          (90,-140),(90,-170),(20,-170),(20,-140),      # 검정  오른쪽(0,1)
          (-85,-140),(-85,-170),(-25,-170),(-25,-140),  # 주황  왼쪽(1,0)
          (85,-140),(85,-170),(25,-170),(25,-140)]      # 주황  오른쪽(1,1)
def drawleg(col, d): 
    if col == 0:      # 검정색
        t.color(line_color, line_color)
    elif col == 1:    # 주황색 안쪽
        t.color(body_color, body_color)
    t.penup()
    t.goto(posleg[col*8+d*4 + 0])
    t.begin_fill()
    t.pendown()
    t.goto(posleg[col*8+d*4 + 1])   
    t.goto(posleg[col*8+d*4 + 2])   
    t.goto(posleg[col*8+d*4 + 3])   
    t.end_fill()

# 발 그리기
posfoot = [(-55, -170),     # 왼쪽(0)
          (55, -170)]       # 오른쪽(1)
def drawfoot(col, d):
    t.penup()
    t.goto(posfoot[d])
    if col == 0:      # 검정색
       t.dot(75, line_color)
    elif col == 1:    # 주황색 안쪽
        t.dot(65, body_color)

# 팔 그리기
poshand = [(-45, -40),      # 왼쪽(0)
          (45, -40)]        # 오른쪽(1)
def drawhand(col, d):
    t.penup()
    t.goto(poshand[d]) 
    if col == 0:      # 검정색
       t.dot(150, line_color)
    elif col == 1:    # 주황색 안쪽
       t.dot(140, body_color)  

# 팔 몸 구분선 그리기
posline = [(-90, -30),(-90, -100),     # 왼쪽(0)
          (90, -30),(90, -100)]        # 오른쪽(1)
def drawhandline(d):
    t.pencolor(line_color)
    t.penup()
    t.goto(posline[d*2 + 0])
    t.pendown()         
    t.goto(posline[d*2 + 1])

# 배 튤립모양 그리기
poschest = [(40,-40),(20,-60),(0,-40),(-20,-60),(-40,-40)] # 지그재그 위치      
def drawflower():
    t.color(chest_color, chest_color)
    t.penup()
    t.goto(poschest[0])
    t.pendown()
    t.begin_fill()
    t.goto(poschest[1])
    t.goto(poschest[2])
    t.goto(poschest[3])
    t.goto(poschest[4])
    t.setheading(240)
    t.circle(47, 240)
    t.end_fill()

# 귀 그리기
posear = [(-80,200),(80,200)]   # 왼쪽, 오른쪽    
def drawear(d):
    t.penup()
    t.goto(posear[d])
    t.dot(50, line_color)
    t.dot(40, body_color)

# 얼굴 그리기
posface = [(0, 100)]    
def drawface():
    t.penup()
    t.goto(posface[0])
    t.dot(250, line_color)
    t.dot(240, body_color)

# 눈 그리기
poseye = [(-80,130),(-30,130),(-55,110),  # 왼쪽 눈썹, 눈 
         (80,130),(30,130),(55,110)]      # 오른쪽 눈썹, 눈 
def draweye(d):
    t.pensize(10)
    t.pencolor(line_color)
    # 눈썹 그리기
    t.penup()
    t.goto(poseye[d*3+0])
    t.pendown()
    t.goto(poseye[d*3+1])
    # 눈 그리기
    t.penup()
    t.goto(poseye[d*3+2])
    t.dot(15, line_color)

# 입과 코 사이 그리기
posmouth = [(-16,62), (16,62)]  # 왼쪽, 오른쪽
def drawmouth(d):
    t.goto(posmouth[d])     
    t.dot(40, line_color)   
    t.dot(29, nose_color)     

# 코 그리기
posnose = [(15,65), (0,77)]  # 중간에 검정이 보기싫어서 흰색칠하기, 코점
def drawnose():  
    # 코와 입 부자연스러운 부분 흰색으로 채우기
    t.pensize(14)
    t.pencolor(nose_color)
    t.penup()
    t.goto(posnose[0])  
    t.setheading(0)
    t.pendown()
    t.back(30)      
    #코 까만점
    t.penup()
    t.goto(posnose[1])   
    t.dot(20, line_color) 


# 검정색 먼저 그리기
drawbody(0)         # 검정색 몸
drawleg(0, 0)       # 왼쪽 다리
drawleg(0, 1)       # 오른쪽 다리
drawfoot(0, 0)      # 왼발
drawfoot(0, 1)      # 오른발
drawhand(0, 0)      # 왼팔
drawhand(0, 1)      # 오른팔

# 주황색 그리기
drawbody(1)         # 주황색 몸
drawleg(1, 0)       # 왼쪽 다리
drawleg(1, 1)       # 오른쪽 다리
drawfoot(1, 0)      # 왼발
drawfoot(1, 1)      # 오른발
drawhand(1, 0)      # 왼팔
drawhand(1, 1)      # 오른팔

drawhandline(0)     # 왼손과 몸 구분선
drawhandline(1)     # 오른손과 몸 구분석
drawflower()        # 가슴 튤립 그리기    

# 머리 그리기 
drawear(0)      # 왼쪽 귀
drawear(1)      # 오른쪽 귀
drawface()      # 얼굴 
draweye(0)      # 왼쪽 눈
draweye(1)      # 오른쪽 눈
drawmouth(0)    # 왼쪽 입, 인중
drawmouth(1)    # 오른쪽 입, 인중
drawnose()      # 코

t.hideturtle()  # 터틀 숨기기
s.update()
s.mainloop()