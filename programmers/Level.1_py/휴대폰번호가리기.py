def solution(s):
    return "*"*(len(s)-4) + s[-4:]

def solution(phone_number):
	return ''.join(['*' for _ in phone_number[:-4]]) + phone_number[-4:]

#numbers에서 끝자리4자리 제외한 수를 *로 변환후 return
# arr                  result
# 010112345678	    *******5678