def coke(n,lost,reserve):
    set_reserve= set(reserve)-set(lost)
    set_lost= set(lost)-set(reserve)
    cnt=0
    
    for i in reserve:
        if lost.count(i)==1:
            cnt+=1
    for j in set_reserve:
        if j-1 ==0:
            pass
        if list(set_lost).count(j+1)==1:
            cnt+=1

    return n-len(lost)+cnt

def solution(n,lost,reserve):
    # 정렬
    lost.sort()
    reserve.sort()
	
    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
	
    # 체육복 빌려주기(나의 앞 번호부터 확인)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    
    return n-len(lost)

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

#n	lost	reserve	return
#5	[2,4]	[1,3,5]	5
#5	[2,4]	[3]	    4
#3	[3]	    [1]	    2

#바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있다고 한다.
# 전체 학생 수 n, 체육복을 도난당한 학생들lost, 여벌의 체육복을 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록