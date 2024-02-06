def coke(keymap,targets,result):
    answer =[]
    for i in targets:
        minkey = 0 # target(i)을 작성하기 위한 총 횟수
        for j in i: 
            c = 101 # 100번까지 가능하므로 101을 max로 초기화
            flag = False # 존재하는지 확인하는 flag
            
            for k in keymap:
                key = k.find(j)
                if key ==-1:
                    continue
                c= min(key+1,c)
                flag = True # 해당 문자열 존재함으로 flag 표시
                
            if flag:
                minkey +=c
            else:
                answer.append(-1)
                break
        else:
            answer.append(minkey) 
                
    return answer

print(coke(["ABACD", "BCEFD"],["ABCD","AABB"],[9, 4]))

# keymap	            targets	            result
# ["ABACD", "BCEFD"]	["ABCD","AABB"]	    [9, 4]
# ["AA"]	            ["B"]	            [-1]
# ["AGZ", "BSSS"]	    ["ASA","BGZ"]	    [4, 6]

#예를 들어, 1번 키에 "A", "B", "C" 순서대로 문자가 할당되어 있다면 1번 키를 한 번 누르면 "A", 두 번 누르면 "B", 세 번 누르면 "C"가 되는 식입니다.
# 문자열배열 keymap과 입력하려는 문자열들이 담긴 문자열 배열 targets가 주어질 때, 각 문자열을 작성하기 위해 키를 최소 몇 번씩 눌러야 하는지 순서대로 배열에 담아 return 하는 solution 함수