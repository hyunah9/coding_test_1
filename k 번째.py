def solution(array,commands):
    answer = []

    for i in range(len(commands)):
        array2 = array[commands[i][0]:commands[i][1]+1]
        array2.sort()
        answer.append(array2[commands[i][2]-1])

    return answer

print(solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]]))