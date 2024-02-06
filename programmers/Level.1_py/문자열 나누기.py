def coke(s):
   answer = 0
   cnt1=0; cnt2=0
   for i in s:
       if cnt1==cnt2:
           answer+=1
           k=i
       if k==i:
           cnt1+=1 # 첫문자 개수
       else:
           cnt2+=1 # 그 이수 문자 개수
       
   return answer

def solution(s):
    j = 0 
    cnt = 0 
    ans =0
    for idx,i in enumerate(s): 
        cnt += 1 if s[j] == i else -1 
        if cnt == 0 : 
            ans +=1 
            j = idx+1 
    return ans + 1 if cnt else ans

print(coke("aaabbaccccabba"))
#처음문자 x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다. 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다
# s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return 하는 함수
#s	result
#"banana"	3           ba - na - na
#"abracadabra"	6       ab - ra - ca - da - br - a
#"aaabbaccccabba"	3   aaabbacc - ccab - ba