###################### Basic rock paper scissor games
'''
import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer )
        print("player: ", player)
        print('Tie!')
    elif player == 'rock':
        if computer == 'paper':
            print("computer: ",computer )
            print("player: ", player)
            print('You lose!')
        if computer == 'scissors':
            print("computer: ",computer )
            print("player: ", player)
            print('You win!')
    elif player == 'paper':
        if computer == 'scissors':
            print("computer: ",computer )
            print("player: ", player)
            print('You lose!')
        if computer == 'rock':
            print("computer: ",computer )
            print("player: ", player)
            print('You win!')
    elif player == 'scissors':
        if computer == 'rock':
            print("computer: ",computer )
            print("player: ", player)
            print('You lose!')
        if computer == 'paper':
            print("computer: ",computer )
            print("player: ", player)
            print('You win!')

    play_again = input('Play again? (yes/no): ').lower()

    if play_again != "yes":
        break 

print("Bye!")

'''

###################### Basic quiz games

'''
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions: 
        print("------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1


    display_score(correct_guesses, guesses)

# ------------------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG")
        return 0


# ------------------------------
def display_score(correct_guesses, guesses):
    
    print("------------------------------")
    print("RESULTS")
    print("------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions)) * 100)
    print("Your score is: "+str(score)+"%")
# ------------------------------
def play_again():
    
    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True 
    else:
        return False


questions = {
    "What the capital of Haiti?: ": "A",
    "What country has Washington DC as their capital?: ": "C",
    "Which one is NOT a Hyndai model?: ": 'B',
    "When did Max get married?: ": 'D',
}

options = [
    ['A. Port-au-Prince', 'B. Las Vegas', 'C. Montana', 'D. Beijin'],
    ['A. Egypt', 'B. Israel', 'C. USA', 'D. Jamaica'],
    ['A. Sonata', 'B. Rx350', 'C. Santa fe', 'D. Elantra'],
    ['A. Jan 15th', 'B. Feb 1st', 'C. Jan 29th', 'D. Jan 30th'],
]


new_game()


while play_again():
    new_game()


print("Play again next time, bye!!!")

'''