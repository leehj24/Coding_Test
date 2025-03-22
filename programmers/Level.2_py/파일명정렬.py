def solution(files):
    tmp = []
    head, number, tail = '', '', ''
    
    for file in files:       
        for i in range(len(file)):
            if file[i].isdigit():     # 숫자가 나오면 그 이전은 무조건 HEAD, 이후는 NUMBER, TAIL로 다시 구분
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):    # NUMBER와 TAIL 구분 (숫자 안나오면 TAIL)
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                        
                tmp.append([head, number, tail])
                head, number, tail = '', '', ''
                break

    tmp = sorted(tmp, key=lambda x:(x[0].lower(), int(x[1])))

    return [''.join(i) for i in tmp]



# 입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# 출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# 입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# 출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

import re

def sol(files):
    a = sorted(files, key=lambda x : int(re.findall('\d+', x)[0]))
    #  files의 각파일 이름(x)에서 숫자(연속된 숫자 부분)를 모두 찾아 리스트로 반환합니다.
    b = sorted(a, key=lambda x : re.split('\d+', x.lower())[0])
    return b 
# 파일 이름을 소문자로 변환해 대소문자를 구분하지 않도록 합니다.
# 예를 들어, "img12.png"는 ["img", ".png"]로 분리됩니다.
# [0]은 리스트의 첫 번째 요소(HEAD 부분)를 가져옵니다.
# HEAD를 기준으로 정렬합니다.

print(sol(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))