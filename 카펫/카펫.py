def solution(brown, yellow):
    for i in range(brown):  #처음에 yellow했음 시간초과, brown 해도 되는이유는?
        for j in range(brown): #이하동문
            if (i+1) * (j+1) == yellow and (i+j+2)*2+4 == brown:
                return [j+3,i+3] # i 와 j 는 0 부터 시작험욿 +1 위아래 두개씩 더해지므로 +2
