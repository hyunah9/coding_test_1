def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    answer = participant[-1]
    for i in range (len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer