def coke(brown, yellow):

    for i in range(1,brown+1):
        for j in range(i+1):
            if j*2+(i-2)*2==brown:
                if (j-2)*(i-2)==yellow:
                    return[i,j]
                
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]

print(coke(8,1))
#가로a 세로b인 카펫이 있다. 테두리는 갈색이 brwon만큼, 안에는  노랑이 yellow 만큼 있다 하였을 때
# 가로 세로를 배열로 return하라

#    a*2+(b-2)*2==brown
#   (a-2)*(b-2)=yellow