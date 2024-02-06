def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
#또는
def solution(spell, dic):
    for i in dic:
        if sorted(list(i)) == sorted(spell):
            return 1
    return 2
#spell=["p", "o", "s"], dic=["sod", "eocd", "qixm", "adio", "soo"] result=2
# spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return