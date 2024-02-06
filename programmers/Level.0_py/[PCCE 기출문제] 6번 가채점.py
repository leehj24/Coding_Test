def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")
    return answer

# numbers	our_score	score_list	                        result
# [1]	    [100]	    [100, 80, 90, 84, 20]	            ["Same"]
# [3, 4]	[85, 93]	[85, 92, 38, 93, 48, 85, 92, 56]	["Different", "Same"]

# 1번 학생이 가채점한 성적은 100점으로 실제 성적과 같기 때문에 "Same"을 담아 return합니다.

# 3번 학생이 가채점한 성적은 85점으로 실제 성적 38점과 다르기 때문에 "Different"를, 
# 4번 학생이 채점한 성적은 93점으로 실제 성적과 같기 때문에 "Same"을 담아 return합니다.