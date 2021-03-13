from collections import Counter
def solution(clothes):
    answer = 1
    kind = []
    for i in range(len(clothes)):
        kind.append(clothes[i][1])
    counter = Counter(kind) #kind의 갯수 세기 
    counter = dict(counter)
    print(counter)
    counter = list(counter.values())
    if len(counter) != 1:
        for k in range(len(counter)):
            answer *= (counter[k]+1)
        return answer -1
    else:
        answer =counter[0]
        return answer