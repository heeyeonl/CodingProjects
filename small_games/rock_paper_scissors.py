import random

def message_computer(computer):    
    switch = {
        0: "Computer: Rock",
        1: "Comptuer: Paper",
        2: "Computer: Scissors"      
    }
    print(switch.get(computer))

def rock_paper_scissors(human):
    if human == 'q':
        return ""
    human = int(human)
    computer = random.randint(0,2)
    message_computer(computer)
    
    if human == computer:
        print("Tie")
    elif (human == 0 and computer == 1) or (human == 1 and computer == 2) or (human == 2 and computer == 0):
        print("You lost!")
    elif (human == 0 and computer == 2) or (human == 1 and computer == 0) or (human == 2 and computer == 1):
        print("You win!")
    else:
        print("error", human, computer)

    return prompt()
    

def prompt():
    print("Rock(0), paper(1), scissors(2) | Enter 'q' to quit")
    human = input("Enter number: ")
    print(rock_paper_scissors(human))


prompt()