# schedule : 출근 희망 시간
# timelogs : 출근 시간
# startday : 시작한요일(1: 월요일, 6, 7 제외) -> startday % 7 -> if 0,6 은 제외 

def solution(schedules, timelogs, startday):
    answer = 0

    for week in range(len(timelogs)):
        success = 0
        day_num = startday
        
        for day in timelogs[week]:
            if day_num % 7 == 0 or day_num % 7 == 6:
                day_num += 1
                continue
        
            limit = schedules[week] + 10
            if limit % 100 >= 60:
                limit += 40
            
            if limit >= day:
                success += 1
            day_num += 1

        if success == 5:
            answer += 1
    return answer