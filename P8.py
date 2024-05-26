#Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations
# to the winner, and ask if the players want to start a new game)
print("Welcome to the game of Rock,Paper and Scissors!Type 'r','p' and 's' respectively! ")
i='start'
while i!='end':
    p1=input("Player 1:")
    p2=input("Player 2:")
    if p1=='r':
        if p2=='s':
            print("rock wins!Congrats player 1!")
        elif p2=='r':
            print("Draw!")
        else:
            print("Paper wins!Congrats player 2!")
    if p1=='s':
            if p2=='r':
                print("rock wins!Congrats player 2!")
            elif p2=='s':
                print("Draw!")
            else:
                print("scissor wins!Congrats player 1!")
    if p1=='p':
        if p2=='s':
            print("scissor wins!Congrats player 2!")
        elif p2=='p':
            print("Draw!")
        else:
            print("Paper wins!Congrats player 1!")
    i = input("Start game?Type start or end: ")








