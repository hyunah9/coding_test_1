import heapq as hq

def solution(scoville, K):

    scoville.sort()
    answer = 0
    while True:
        first = hq.heappop(scoville) #제일작은수 뽑고 삭제
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2) #그자리에 넣기
        answer += 1  

    return answer