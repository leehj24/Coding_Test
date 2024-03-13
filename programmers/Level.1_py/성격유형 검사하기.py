def solution(survey, choices):
    types = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(choices)):
        if choices[i] < 4:
            types[survey[i][0]] += (choices[i] * 3) % 4
        if choices[i] > 4:
            types[survey[i][1]] += choices[i] % 4
    type_key = list(types.keys())
    
    answer = ''
    for i in range(0, len(type_key), 2):
        if types[type_key[i]] > types[type_key[i+1]]:
            answer += type_key[i]
        elif types[type_key[i]] < types[type_key[i+1]]:
            answer += type_key[i+1]
        else:
            answer += min(type_key[i], type_key[i+1])
    return answer

def solution(survey, choices):
    answer = ''
    dic= {"R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 }
    
    for s,c in zip(survey,choices):
        if c>4:     dic[s[1]] += c-4
        elif c<4:   dic[s[0]] += 4-c
    
    li = list(dic.items())
    
    for i in range(0,8,2):
        if li[i][1] < li[i+1][1]: answer += li[i+1][0]
        else:   answer += li[i][0]
        
    return answer

# survey의 원소는 "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 중 하나입니다.
# choices	뜻
# 1	매우 비동의
# 2	비동의
# 3	약간 비동의
# 4	모르겠음
# 5	약간 동의
# 6	동의
# 7	매우 동의
# 질문마다 판단하는 지표를 담은 1차원 문자열 배열 survey와 검사자가 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 choices가 
# 매개변수로 주어집니다. 이때, 검사자의 성격 유형 검사 결과를 지표 번호 순서대로 return 하도록 solution 함수를 완성해주세요.

# survey	choices	result
# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"
# ["TR", "RT", "TR"]	[7, 1, 3]	"RCJA"

