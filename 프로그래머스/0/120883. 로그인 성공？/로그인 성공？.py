def solution(id_pw, db):
    answer = ''
    id_in = id_pw[0]
    pw_in = id_pw[1]
    for id, pw in db:
        if id == id_in and pw == pw_in:
            answer = 'login'
            break
        elif id == id_in and pw != pw_in:
            answer = 'wrong pw'
            break
        else:
            answer = 'fail'
    return answer