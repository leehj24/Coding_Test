
def solution(n):
    answer = 0
    one_count = bin(n).count("1")
    
    for num in range(n+1, 1000001):
        num_one_count = bin(num).count("1")
    
        if one_count == num_one_count:
            answer = num
            break
        
    return answer
#n  answer
#78 83
    
    
def solution(n):
    c = n+1
    while True:
        if bin(c).count('1') == bin(n).count('1'):
            return c
        c += 1

#연속된 자연수들로 n을 표현하는 방법의 수

def setDefaultMsg(self):
    self.scenarioDict = dict()

    for msgName, valueDict in self.checkDB.items():
        scenarioValues = list()
        dbc = valueDict[0]
        scenarioDefault = dbc.get_message_by_name(msgName)

        for signal in scenarioDefault.signals:
            if (str(signal.initial) == "None"):
                scenarioValues.append(str(signal.offset))
            else:
                pass

        self.scenarioDict[scenarioDefault] = scenarioValues
        

def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key = lambda x : ((x[1]+x[0])/x[0],x[1]))
    for x,y in dungeons:
        print("x :", x, "y : ", y)
        if k >= x:
            k -= y
            answer += 1
    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))
