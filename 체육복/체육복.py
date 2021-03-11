def solution(n, lost, reserve):
    for m in lost:
        if m in reserve:
            lost.remove(m)
            reserve.remove(m)

# 여분이 있고 잃어버리면 1개를 가지고 있는것과 마찬가지이기 때문에
    answer = n-len(lost) #여분이 있는 명 수
    for i in range(len(lost)):
        for k in range(len(reserve)):
            if lost[i] == reserve[k] or lost[i]==reserve[k]-1 or lost[i]==reserve[k]+1: 
                #[1,2,3,4][1,2,3]인 경우 2는 위의 for 문에서 remove안된다.
                reserve[k]=-10
                answer = answer +1
                break
    
    return answer