def solution(people, limit):
    answer = 0
    ans = 0
    ans3= 0
    ans2 = len(people)-1
    people.sort()
    while (ans<ans2):
        if people[ans] + people[ans2] <=limit:
            ans += 1
            ans3 +=1
        ans2 -=1
    answer = len(people)- ans3*2 +ans3
    return answer