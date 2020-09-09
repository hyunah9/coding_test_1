def solution(n, lost, reserve):

    for m in lost:
        if m in reserve:
            lost.remove(m)
            reserve.remove(m)

    answer = n-len(lost)
    for i in range(len(lost)):
        for k in range(len(reserve)):
            if lost[i]==reserve[k] or lost[i]==reserve[k]-1 or lost[i]==reserve[k]+1:   # k 가 2이면 lost[0]=3일때 두번째에 성립하므로
                reserve[k]=-10
                answer = answer +1
                break
    return answer

print(solution(3,[1,2],[2,3]))
