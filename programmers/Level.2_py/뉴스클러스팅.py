import re

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    a = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    b = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    if len(a)==0 and len(b):
        j = 1
    else:
        # 다중합집합
        a_temp = a.copy()
        a_result = a.copy()
        for i in b:
            if i not in a_temp: # B에만 존재하면 합집합에 추가
                a_result.append(i) 
            else: # 공통으로 존재하면 중복되므로 제거
                a_temp.remove(i)
        # 다중교집합
        result = []
        for i in b:
            if i in a:
                a.remove(i)
                result.append(i)

        j = len(result)/len(a_result) # 자카드 유사도 = 교집합/합집합
        
    return (int(j * 65536))

print(solution("FRANCE","french"))

######
from collections import Counter
def solution(str1, str2):
    # make sets
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
    return answer

###
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
#문자열을 두개식 묶어 두 문자의 교집합/합집합을 65536곱하여 return
#두개씩 묶었을 경우 문자가 영어가 아니면 그 문자는 버린다. [ab,b-]는 [ab,b]가 된다
# "FRANCE"    "french"    16384
# "E=M*C^2"	"e=m*c^2"	65536
