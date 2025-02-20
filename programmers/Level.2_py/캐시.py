def check(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        city = city.lower()
        if cacheSize:
            if not city in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                time += 5
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
        else:
            time += 5
    return time

##

def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time

print(check(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo"," Seoul", "Jeju", "Pangyo", "Seoul"]))

#입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력한다.
#miss하면 5, hit하면 1씩 시간이 증가된다