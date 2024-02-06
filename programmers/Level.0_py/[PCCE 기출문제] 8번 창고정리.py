def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            clean_num.append(num[i])
            
    # 아래 코드에는 틀린 부분이 없습니다.
            
    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer

#storage						                num			        result
# ["pencil", "pencil", "pencil", "book"]	    [2, 4, 3, 1]		"pencil"
# ["doll", "doll", "doll", "doll"]			    [1, 1, 1, 1]		"doll"
# ["apple", "steel", "leaf", "apple", "leaf"]	[5, 3, 5, 3, 7]	    "leaf"
# ["mirror", "net", "mirror", "net", "bottle"]	[4, 1, 4, 1, 5]	    "mirror"

# 정리함에 있는 물건이 각각 개수가 num 만큼 있다 하였을 때 가장 많은 물건을 return 