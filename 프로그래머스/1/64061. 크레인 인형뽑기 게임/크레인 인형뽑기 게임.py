def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        for i in range(len(board)):
            # move는 1부터 시작하기에, move-1 진행하기
            if board[i][move-1] != 0:
                basket.append(board[i][move-1])
                board[i][move-1] = 0
                
                if len(basket) >= 2:
                    a = basket[-1]
                    b = basket[-2]
                    if a == b:
                        # 인형은 2개 터지기에, answer += 2
                        answer += 2
                        basket.pop()
                        basket.pop()
                break
    return answer