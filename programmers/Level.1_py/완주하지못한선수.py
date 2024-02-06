def coke(Participant,Completion):
    for i in Completion:
        Participant.remove(i)
    return "".join(Participant)


def coke(participant,completion):

    # 1. 두 list를 sorting한다
    participant.sort()
    completion.sort()

    # 2. completeion list의 len만큼 participant를 찾아서 없는 사람을 찾는다
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수이다.
    return participant[len(participant)-1]


import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

print(coke(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

# Participant							            Completion					                Return
#["leo", "kiki", "eden"]					        ["eden", "kiki"]					        "leo"
#["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
#["mislav", "stanko", "mislav", "ana"]			    ["stanko", "ana", "mislav"]			"       mislav
#마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수
