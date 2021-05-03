def solution(s):
    answer = ''
    s1 = s.lower()
    s1 = s1.split(' ')
    for i in s1:
        i= i + ' '
        if i[0].isalpha() == True:
            i = i[0].upper() + i[1:]
        answer += i
    answer = answer.rstrip()
    if s[len(s)-1] == ' ':
        answer += ' '
    return answer