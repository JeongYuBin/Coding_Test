def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    my_string = sorted(my_string)
    for i in range(len(my_string)):
        answer+= my_string[i]
    return answer

# ''.join : return += 안하고 바로 return 에 넣기 