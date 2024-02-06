def coke(k,box):
    answer = 0
    a={}
    
    for i in box:
        if i in a:  # a안에 i가 있으면
            a[i]+=1 # a[i]값을 1씩 증가 (ex: 1:1, 3:1 이였디면 1:1, 3:2)
        else:
            a[i]=1  #a[i]값을 1로 저장
            
    # dict된 a를 item으로 묶은후, a[i] 값만 불러와 내림순으로 배열한 값을 dict
    #a.items()는 dict_items([(1, 1), (3, 2), (2, 2), (5, 2), (4, 1)])이다
    
    a= dict(sorted(a.items(),key = lambda x:x[1],reverse=True))
    
    for i in a:
        if k <=0:
            return answer
        k-=a[i]     #귤 k개수에서 a[i]값 만큼 뺀다
        answer +=1
    return answer

print(coke(6,[1, 3, 2, 5, 4, 5, 2, 3]))

#[1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 경화가 귤 6개를 판매하고 싶다면, 
# 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 
# 귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.