import tictactoe

players = ['x', 'o']

if __name__ == "__main__":
    ttt = tictactoe.TicTacToe(players)
    winner = None
    run = True
    while run:
        ttt.print()
        move = int(input())
        over, winner = ttt.play(move)
        if over:
            run = False
    ttt.print()
    if winner:
        print(f'Congratulations Player {winner} for winning the game!')
    else:
        print(f"It's a tie!")
