def solution(today, terms, privacies):
    answer = []
    
    for i in range(len(privacies)):
        date, grade = privacies[i].split(' ')
        year, month, day = map(int, date.split('.'))
        
        for j in range(len(terms)):
            gr, mo = terms[j].split(' ')
        
            if grade == gr:
                mo = int(mo)
                break
        month = month + mo
        day -= 1 
        while month >= 13:
            month -= 12
            year += 1
        if day == 0:
            month -= 1
            day += 28
            if month == 0:
                year -= 1
                month += 12
        
        deadline = f"{year}.{month:02d}.{day:02d}"
        if today > deadline:
            answer.append(i+1)
    
    return answer