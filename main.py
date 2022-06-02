import random

while True:
    outcomes = {"R": "Rock","P":"Paper", "S":"Scissors"}
    input_list = ['R','P','S','Q']
    print('Rock, paper, Scissors depiction')
    user_input = input("Enter 'R' for rock, 'P' for paper or 'S' for scissors, Q to Terminate Game: ")
        
    if user_input not in input_list:
        print('Invalid choice. Try again')
        user_input = input("Enter 'R' for rock, 'P' for paper or 'S' for scissors, Q to Terminate Game: ")
            
    comp_choice = random.choice(input_list)
    print(f"Player({outcomes[user_input]}): CPU({outcomes[comp_choice]})")
        
    if user_input == comp_choice:
        print(f"It's a tie {user_input}")
    elif (user_input =="R" and comp_choice =="S") or (user_input =="P" and comp_choice == "R") or (user_input == "S" and comp_choice == "P"):
        print('User wins')
    else:
        print('Computer wins')
    if user_input == "Q":
        break