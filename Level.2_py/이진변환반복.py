def coke(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]

def solution(x):
    answer = []
    
    cnt = 0
    zero = 0
    
    while True:
        if x == '1':
            break
        zero = zero + x.count("0")
        x = x.replace("0", "")
        
        x = bin(len(x))[2:]
        
        cnt = cnt + 1
    
    answer = [cnt, zero]
    
    return answer

print(coke("110010101001"))

#문자열에 0을 제거, 제거한 이진법을 10진법으로 변환후 다시 0을 제거하는 것을 s="1"이
# 될때까지 반복한다. 이진변환의 횟수와 변환과정에 제거된 모든 0의 개수를 배열에 담아 return

#회차	이진 변환 이전	 제거할 0의 개수	  0 제거 후 길이	이진 변환 결과
# 1	    "110010101001"	 6				    6			      "110"
# 2	    "110"			 1				    2			      "10"
# 3	    "10"			 1				    1			      "1"
