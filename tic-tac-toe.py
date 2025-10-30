def play(board):
    x_count = board.count('x')
    o_count = board.count('o')
    current_player = 'x' if x_count == o_count else 'o'
    
    lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    for line in lines:
        values = [board[i] for i in line]
        if values.count(current_player) == 2 and values.count('') == 1:
            return line[values.index('')]
    
    opponent = 'o' if current_player == 'x' else 'x'
    for line in lines:
        values = [board[i] for i in line]
        if values.count(opponent) == 2 and values.count('') == 1:
            return line[values.index('')]
    
    if board[4] == '': return 4
    corners = [0,2,6,8]
    for corner in corners:
        if board[corner] == '': return corner
    for i in range(9):
        if board[i] == '': return i
