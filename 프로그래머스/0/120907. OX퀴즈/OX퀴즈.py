def solution(quiz):
    answer = []
    for i in quiz:
        i = i.split()
        if i[1] == '-':
            if int(i[0]) - int(i[2]) == int(i[4]):
                answer.append('O')
            else:
                answer.append('X')
        if i[1] == '+':
            if int(i[0]) + int(i[2]) == int(i[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer