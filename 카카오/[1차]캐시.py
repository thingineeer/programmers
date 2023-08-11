# 1차 캐시
 
from collections import deque
 
def solution(cacheSize, cities):
    cache = deque([])
    cities = map(lambda x: x.lower(), cities)  # 모두 소문자로 구분
    hit = 1
    miss = 5
    result = 0
 
    for i in cities:
        if not i in cache and len(cache) < cacheSize:  # 1. 캐시에 없는데, 캐시크기를 초과하지 않은 경우
            cache.append(i)
            result += miss
        elif not i in cache and len(cache) >= cacheSize: # 2. 캐시에 없는데,  캐시크기를 초과한 경우
            cache.append(i)
            cache.popleft()
            result += miss
        else: # 3. 캐시에 있는 경우
            result += hit
            cache.remove(i)
            cache.append(i)
 
    return result
