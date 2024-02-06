def solution(picture, k):
    answer = []
    
    for i in picture:
        char = ""
        for j in i:
            char += j*k
        for c in range(k):
            answer.append(char)
    
    return answer

#문자열을 k베 늘린후 추출
#picture =["x.x", ".x.", "x.x"]	 k= 3	
# result = ["xxx...xxx", "xxx...xxx", "xxx...xxx", "...xxx...", "...xxx...", 
# "...xxx...", "xxx...xxx", "xxx...xxx", "xxx...xxx"]