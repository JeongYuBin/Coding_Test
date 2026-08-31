def solution(a, b):
    day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    week = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    val = b
    for i in range(a):
        val += day[i]
    answer = week[val%7]
    
    return answer