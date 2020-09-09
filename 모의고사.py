def solution(answers):
    answer = []
    count = {1: 0, 2: 0, 3: 0}  # 1을 0이라고하고 2도 0 3도 0 이라고한다
    forgiver1 = [1, 2, 3, 4, 5] * 2000
    forgiver2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    forgiver3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    for i in range(10000):
        if answers[i%len(answers)] == forgiver1[i]:
            count[1] += 1
        if answers[i%len(answers)] == forgiver2[i]:
            count[2] += 1
        if answers[i%len(answers)] == forgiver3[i]:
            count[3] += 1

    max_value = max(count.values())
    for key, value in count.items():  # item은 요소 value 큰값 비교해서 key 를 반환해야하므로
        if value == max_value:
            answer.append(key)
    return answer

print(solution([1, 2, 3, 4, 5]))  # 정답은 1,2,3,4,5