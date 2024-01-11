def solution(id_pw, db):
    for i in db:
        # id 여부 확인
        if id_pw[0] in i:
            if id_pw[1] == i[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"

# id_pw	                            db	                        result
# ["meosseugi", "1234"]	        [["rardss", "123"],             "login"
#                               ["yyoom", "1234"], 
#                               ["meosseugi", "1234"]]	

# ["programmer01", "15789"]	    [["programmer02", "111111"],    "wrong pw"
#                               ["programmer00", "134"], 
#                               ["programmer01", "1145"]]	

# ["rabbit04", "98761"]	        [["jaja11", "98761"],           "fail"
#                               ["krong0313", "29440"], 
#                               ["rabbit00", "111333"]]	