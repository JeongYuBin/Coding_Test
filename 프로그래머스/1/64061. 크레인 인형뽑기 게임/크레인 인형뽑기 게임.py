def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                basket.append(board[i][move-1])
                board[i][move-1] = 0
                
                if len(basket) >= 2:
                    a = basket[-1]
                    b = basket[-2]
                    if a == b:
                        answer += 2
                        basket.pop()
                        basket.pop()
                break
    return answer