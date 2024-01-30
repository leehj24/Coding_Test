def solution(s):
    array = s.split()
    jaden= []
    for i in array:
        jaden.append(i.capitalize())
    return " ".join(jaden)

def solution(s):
    return s.title()

def solution(s):
    answer =[]
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:]) 
    return " ".join(answer)

#단어의 첫문자를 대문자로 변경하여 return
#s	                        return
#"3people unFollowed me"	"3people Unfollowed Me"
#"for the last week"	    "For The Last Week"
