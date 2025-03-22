def coke(lottos,win_ums):
    grade={1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    m_in=0 ; m_ax=0
    
    for i in lottos:
        if i in win_ums:
            m_in+=1
    
    for j in lottos:
        print(j)
        if j in win_ums:
            print(m_ax,j)
            m_ax+=1
        elif j ==0:
            print(m_ax,j)
            m_ax+=1

    if m_in == 0:
        m_in = 1
    array=[grade[m_ax],grade[m_in]]
    return array

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

print(coke([31,3,4,5,7,0],[31, 10, 45, 1, 6, 19]))

#새로산 lottos배열에서 모르는 수는 0이며 발표난 로또win_nums 이라 하였을때 0의 수에 따라 최고순위와 최저순위를 return
# 1등-6개일치, 2등-5개일치, 3등-4개일치, 4등-3개일치, 5등-2개일치, 6등 낙첨
#lottos	                win_nums	                result
#[44, 1, 0, 0, 31, 25]  [31, 10, 45, 1, 6, 19]	    [3, 5]
#[0, 0, 0, 0, 0, 0]	    [38, 19, 20, 40, 15, 25]	[1, 6]

def solution(lottos, win_nums):
    answer = []
    count=0 # 0이 있을때 같은거 찾는 수 
    count2 = 0 # 0이 없을때 같은거 찾는 수 
    for i in lottos:
        if i == 0:
            count+=1 #0인걸 win과 같을때 추가
            if i in win_nums:
                count +=1 #0이 win과 같고 lotto가 win에 있을때
        else: # 0 아닌 부분에서
            if i in win_nums:
                print(i,"j")
                count +=1 # 0이 추가된 상테에서 lotto가 win에 있을때
                count2 +=1 # 0이 없는 상테에서 lotto가 win에 있을때
            
    loto_win = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    for i in loto_win:
        if i == count:
            answer.append(loto_win[i])
        if i == count2:
            answer.append(loto_win[i])
    answer.sort()
    return answer