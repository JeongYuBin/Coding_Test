# ext : 어떤 정보를 기준으로 뽑을지
# val_ext : 뽑은 정보의 기준
# sort_by : 정렬 기준 
# ext 값이 val_ext 보다 작아야 하고, sort_by 기준으로 오름차순으로 정렬하기
def solution(data, ext, val_ext, sort_by):
    answer = []
    
    if sort_by == "code":
        value = 0
    elif sort_by == "date":
        value = 1
    elif sort_by == "maximum":
        value = 2
    else:
        value = 3
        
    if ext == "code":
        ext_idx = 0
    elif ext == "date":
        ext_idx = 1
    elif ext == "maximum":
        ext_idx = 2
    else:
        ext_idx = 3
    
    for i in range(len(data)):
        data.sort(key=lambda x:x[value])
    
    for d in data:
        if d[ext_idx] < val_ext:
            answer.append(d)

    return answer