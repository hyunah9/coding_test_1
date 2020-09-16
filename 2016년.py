def getDayName(a,b):
    answer = ""
    if a>=2:
        b+=31
        if a>=3:
            b+=29#2월
            if a>=4:
                b+=31#3월
                if a>=5:
                    b+=30#4월
                    if a>=6:
                        b+=31#5월
                        if a>=7:
                            b+=30#6월
                            if a>=8:
                                b+=31#7월
                                if a>=9:
                                    b+=31#8월
                                    if a>=10:
                                        b+=30#9월
                                        if a>=11:
                                            b+=31#10월
                                            if a==12:
                                                b+=30#11월
    b=b%7

    if b==1:answer="FRI"
    elif b==2:answer="SAT"
    elif b==3:answer="SUN"
    elif b==4:answer="MON"
    elif b==5:answer="TUE"
    elif b==6:answer="WED"
    else:answer="THU"
    return answer


print(getDayName(5,24))

# def solution(a, b):
#     answer = ''
#     date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
#     date_num31 = [5, 7, 8, 10, 12]
#     date_num30 = [4, 6, 9, 11]
#     c = (b % 7 ) - 1
#
#     if 1 <= a <= 12 and 1 <= b <= 31:
#         if a == 1:  # 기준은 금
#             for i in range(7):
#                 if c == i:
#                     answer = date[(c)]
#                     break
#         elif a == 2:  # 기준은 월 즉 DATE[3]
#             for i in range(7):
#                 if c == i:
#                     answer = date[(c + 3) %7]
#                     break
#         elif a == 3:
#             for i in range(7):
#                 if c == i:
#                     answer = date[(c + 1) %7]
#                     break
#
#         elif a == 5 or 7 or 8 or 10 or 12:
#             for p in range(5):
#                     if date_num31[p] == 5:
#                         for i in range(7):
#                             if c == i:
#                                 answer = date[(c + 3 )%7]
#                                 break
#                     elif date_num31[p] == 7:
#                         for i in range(7):
#                             if c == i:
#                                 answer = date[(c + 5)%7]
#                                 break
#                     elif date_num31[p] == 8:
#                         for i in range(7):
#                             if c == i:
#                                 answer = date[(c +5)%7]
#                                 break
#                     elif date_num31[p] == 10:
#                         for i in range(7):
#                             if c == i:
#                                 answer = date[(c + 8)%7]
#                                 break
#                     elif date_num31[p] == 12:
#                         for i in range(7):
#                             if c == i:
#                                 answer = date[(c + 11)%7]
#                                 break
#         elif a == 4 or 6 or 9 or 11:
#             for o in range(4):
#                     if date_num30[o] == 4:
#                         for i in range(7):
#                             if c == i:
#                                 answer = date[(c + 2 )%7]
#                                 break
#                     elif date_num30[o] == 6:
#                         for i in range(7):
#                             if c == i:
#                                 answer = date[(c + 4)%7]
#                                 break
#                     elif date_num30[o] == 9:
#                         for i in range(7):
#                             if c == i:
#                                 answer = date[(c + 10)%7]
#                                 break
#                     elif date_num30[o] == 11:
#                         for i in range(7):
#                             if c == i:
#                                 answer = date[(c+ 12)%7]
#                                 break
#     return answer
#
# print(solution(5,24))
