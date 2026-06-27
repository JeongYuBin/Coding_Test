# 초로 바꾸어서 계산하기 

def solution(video_len, pos, op_start, op_end, commands):
    minute, sec = pos.split(':')
    st_min, st_sec = op_start.split(':')
    end_min, end_sec = op_end.split(':')
    video_min, video_sec = video_len.split(':')
    minute = int(minute)
    sec = int(sec)
    st_min = int(st_min)
    st_sec = int(st_sec)
    end_min = int(end_min)
    end_sec = int(end_sec)
    video_min = int(video_min)
    video_sec = int(video_sec)
    
    time = minute*60+sec
    start = st_min*60+st_sec
    end = end_min*60+end_sec
    video = video_min*60+video_sec

    for word in commands:
        if start <= time <= end:
            time = end
        if word == 'prev':
            time = max(0, time -10)
        elif word == 'next':
            time = min(video, time+10)
        if start <= time <= end:
            time = end
    minute = time // 60
    second = time % 60

    return f"{minute:02d}:{second:02d}"