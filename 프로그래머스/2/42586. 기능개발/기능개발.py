# 배포시, 몇 개의 기능을 동시에 배포하는지 return 하기 
def solution(progresses, speeds):
    answer = []
    day = [] # 배포가 가능한 날짜
    for i in range(len(progresses)):
        val = 100 - progresses[i]
        date = val // speeds[i]
        if val % speeds[i] != 0:
            date += 1   
        day.append(date)  # 작업 끝나는 날짜 저장   
        
    j = 0   # 날짜
    while j < len(day):
        temp = 1 # 배포 처음 기준
        for k in range(j+1, len(day)):
            if day[k] <= day[j]:
                temp += 1 
            else:
                break
        answer.append(temp)
        j += temp
    
    return answer