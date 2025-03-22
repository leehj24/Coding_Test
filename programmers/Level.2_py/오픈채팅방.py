
def sol(record):
    answer=[]
    user={}
    for i in record:
        if i.split()[0]=="Enter":
            user[i.split()[1]]=i.split()[2]
        elif i.split()[0]=="Change":
            user[i.split()[1]]=i.split()[2]

    for i in record:
        if i.split()[0]=="Enter":
            answer.append(user[i.split()[1]]+"님이 들어왔습니다.")
        elif i.split()[0]=="Leave":
            answer.append(user[i.split()[1]]+"님이 나갔습니다.")
    return answer


sol(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
     "Enter uid1234 Prodo","Change uid4567 Ryan"])


# 입출력 예
# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
#           "Enter uid1234 Prodo","Change uid4567 Ryan"]

# return = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", 
# "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# uid를 보고 닉네임을 바꾸거나, 입장/퇴장을 알려주는 문제
# Enter, Leave, Change로 구분되며, Enter와 Leave는 uid와 닉네임이 주어지고
# Change는 uid와 닉네임만 주어진다.
# Enter는 입장, Leave는 퇴장, Change는 닉네임을 바꾸는 것이다.


