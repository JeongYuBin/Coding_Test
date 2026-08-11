def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0]
        end = commands[i][1]
        target = commands[i][2]
        value = array[start-1:end]
        value.sort()
        answer.append(value[target-1])
        
    return answer