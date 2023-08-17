def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
#또는 
def solution(hp):
    a=int(hp/5)
    b=int((hp-5*a)/3)
    c=hp-5*a-b*3
    return a+b+c
#장군개미는 공격력이 5 병장개미는 공격력이 3 일개미는 공격력이 1일 때 개미군단이 몇마리가 필요한지 return
# hp=23, result=5
# hp=999, result=201