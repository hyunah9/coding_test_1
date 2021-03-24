def solution(skill, skill_trees):
    answer = len(skill_trees)
    for i in range(len(skill_trees)) :
        tmp = []
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                tmp.append(skill_trees[i][j])
        print(tmp)
        if len(tmp) == 0: #아무것도안겹치는경우  
            continue
        else:
            for k in range(len(tmp)):   
                if tmp[k] != skill[k]:
                    answer -= 1
                    break
    return answer