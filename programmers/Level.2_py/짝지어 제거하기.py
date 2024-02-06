def coke(s):
    sta=[]
    for i in s:
        if len(sta)==0:
            sta.append(i)
        elif sta[-1]==i:
            sta.pop()
        else:
            sta.append(i)
    if sta:
        return 0
    return 1
print(coke("cdcd"))
#문자열에서 맨앞에 있는 같은 알파벳이 2개 붙어 있는 짝을 제거하고 
# 앞뒤로 문자열을 이어붙인다. 이 과정을 반복하여 문자열을 모두 제거한다.
#문자열이 제거가 되면 1 제거가 되지 않으면 0을 return하라

# s         result
# "baabaa"   1
# "cdcd"     0