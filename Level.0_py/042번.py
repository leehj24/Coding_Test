def solution(my_strings, parts):
    answer = ""
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]
    return answer

# my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
#parts = [[0, 4], [1, 2], [3, 5], [7, 7]]
#result = "programmers"