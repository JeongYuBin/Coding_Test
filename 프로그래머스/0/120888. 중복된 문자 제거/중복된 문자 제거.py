def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
            # append : 리스트 전용
    return answer