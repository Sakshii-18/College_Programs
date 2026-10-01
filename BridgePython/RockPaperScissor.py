print("Enter Your Choice: rock/paper/scissor")

choice1 = input("Player 1: ").lower()
choice2 = input("Player 2: ").lower()

match choice1, choice2:

    case ('rock', 'scissor') | ('scissor', 'paper') | ('paper', 'rock'):
        print("Player 1 wins")

    case ('scissor', 'rock') | ('paper', 'scissor') | ('rock', 'paper'):
        print("Player 2 wins")

    case ('rock', 'rock') | ('paper', 'paper') | ('scissor', 'scissor'):
        print("Draw")

    case _:
        print("Invalid choice")