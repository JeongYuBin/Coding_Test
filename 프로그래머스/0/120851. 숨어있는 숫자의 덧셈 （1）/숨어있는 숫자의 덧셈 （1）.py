def solution(my_string):
    answer = 0
    for i in my_string:
        if i in '0123456789':
            answer += int(i)
    return answer