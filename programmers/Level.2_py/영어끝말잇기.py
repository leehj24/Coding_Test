def coke(n,words):
    for i in range(1, len(words)):
        #글자가 맞지 않을 때
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    return [0,0]

print(coke(2,["hello", "one", "even", "never", "now", "world", "draw"]))

# 사람수가 n이며 순서대로 말한단어가 words라 할때
# 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 

# n	words	                                                                        result
# 3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]
