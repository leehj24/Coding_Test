def coke(babbling):
    answer = 0

    for word in babbling:
        for pro in ["aya", "ye", "woo", "ma"]:
            if pro * 2 not in word:
                word=word.replace(pro,'1')
        if word.isdigit():
            answer+=1

    return answer

def solution(babbling):
    count = 0

    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue    
        if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""):
            count += 1

    return count

print(coke(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
#["ayaye", "uuuma", "yeye", "yemawoo", "ayaayaa"]에서 발음할 수 있는 것은 2개 이다.
#"aya" + "ye" = "ayaye",
#"ye" + "ma" + "woo" = "yemawoo"
#"yeye"는 같은 발음이 연속되므로 발음할 수 없다.
