def solution(cards1,cards2,goal):
    answer = []
    n = len(cards1)
    m = len(cards2)
    
    i = j = 0
    for word in goal:
        if i < n and word == cards1[i]:
            answer.append(cards1[i])
            i += 1
            
        if j < m and word == cards2[j]:
            answer.append(cards2[j])
            j += 1
        
    return 'Yes' if answer == goal else 'No'

def solution(cards1, cards2, goal):
    for word in goal:
        if len(cards1)>0 and cards1[0]==word:
            cards1.pop(0)
        elif len(cards2)>0 and cards2[0]==word:
            cards2.pop(0)
        else:
            return "No"
        
    return "Yes"

# 첫번째 카드["i", "drink", "water"], 두 번째 카드 ["want", "to"]가 적혀있을 때 ["i", "want", "to", "drink", "water"] 순서의 단어 배열을 만들려고 한다면 첫 번째 카드 뭉치에서 "i"를 사용한 후 두 번째 카드 뭉치에서 "want"와 "to"를 사용하고 첫 번째 카드뭉치에 "drink"와 "water"를 차례대로 사용하면 원하는 순서의 단어 배열을 만들 수 있습니다.
# cards1                    canrds2         goal                                    result
# ["i", "drink", "water"]   ["want", "to"]  ["i", "want", "to", "drink", "water"]   "Yes"
# ["i", "water", "drink"]   ["want", "to"]  ["i", "want", "to", "drink", "water"]   "No"
                                      