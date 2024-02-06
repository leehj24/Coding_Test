def coke(p,limit):
    cnt=0
    p.sort() # 숫자 순으로 정렬
    
    start =0
    end = len(p)-1
    
    while(start <= end):
        if p[start]+p[end]<=limit: # 맨 앞과 맨뒤 더한값이 limit 보다 작으면
            start+=1               # 앞뒤로 한칸씩 건다
            end-=1
        else:                      # 그렇지 않으면
            end-=1                 # 맨뒤칸만 앞으로 간다
        cnt+=1                     # 맨앞과 맨뒤 인덱스가 같아질때 까지 숫자 증가
    return cnt
print(coke([70, 50, 80, 50,40,40,80],100))

#구명보트에 두명씩 밖에 못타고, 무게제한limit 가 있다.
# 구명보트를 몇번 태워야 하는지 return하라
# people                        return
#[70, 50, 80, 50,40,40,80]      5