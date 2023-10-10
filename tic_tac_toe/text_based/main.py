import tictactoe

ttt = tictactoe.TicTacToe()
run = True
while run :
    ttt.print()
    print("enter you move: ")
    move =  int(input())
    ttt.play(move)
    over,winner = ttt.evaluate()
    if over: 
        run = False
if winner:
    print(f"congratulations player {winner} for winning the game!")
else:
    print("its a tie!!!")
