# def solution(s):
#     answer = True
#     s2 = s.lower()
#     a = 0
#     b = 0
#     for i in s2:
#         if i == 'p':
#             a+=1
#         elif i == 'y':
#             b+=1
#     print(a,b)
#     if a==b :
#         return answer
#     elif a !=b:
#         answer = False
#         return answer

def numPY(s):
    return s.lower().count('p') == s.lower().count('y')