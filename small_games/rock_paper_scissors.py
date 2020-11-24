import random

def print_message(msg, computer):
    if msg == 'win':
        print("You win! Computer gave", computer)
    elif msg == 'lost':
        print("You lost... Computer gave", computer)
    else:
        print("error in print_message")

def computer_gives(computer):    
    switch = {
        0: "rock",
        1: "paper",
        2: "scissors"      
    }
    return switch.get(computer)

def rock_paper_scissors(human):
    human = human.lower()
    if human == 'q':
        return print("Exit")

    computer = computer_gives(random.randint(0,2))
    
    if human == computer:
        print("Tie!")
    elif human == 'rock':
        if computer == 'scissors':
            print_message('win', computer)
        else:
            print_message('lost', computer)
    elif human == 'paper':
        if computer == 'rock':
            print_message('win', computer)
        else:
            print_message('lost', computer)
    elif human == 'scissors':
        if computer == 'paper':
            print_message('win', computer)
        else:
            print_message('lost', computer)
    else:
        print("Invalid input! Check your spelling.")

    return prompt()
    

def prompt():
    print("Rock, paper, scissors | Enter 'q' to quit")
    human = input("Enter: ")
    rock_paper_scissors(human)


prompt()