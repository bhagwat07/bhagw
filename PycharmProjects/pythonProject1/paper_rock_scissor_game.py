#ROCK,PAPER,SCISSORS GAME


import random

def get_choice():
    player_choice= input('Enter a choice(rock,paper,scissors): ').lower()
    options = ['rock','paper','scissors']
    computer_choice= random.choice(options)
    choices = {'player':player_choice,'computer':computer_choice}
    return choices


def check_win(player,computer):

    print(f'You chose {player},computer chose {computer}')
    #if two values are equal,declare a tie!
    if player == computer:
        return "It's a tie!"

    #check for all possibility when player chose rock...
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes scissors! You win!'
        else:
            return 'paper cover rock! You lose.'
    # check for all possibility when chose paper...
    elif player == 'paper':
        if computer == 'rock':
            return 'paper cover rock! You win!'
        else:
            return 'scissor cut paper! You lose.'
    # check for all possibility when chose scissors...
    elif player == 'scissors':
        if computer == 'paper':
            return 'scissor cut paper! You win!'
        else:
            return 'rock smashes scissors! You lose.'

while True:
    choices = get_choice()
    result = check_win(choices['player'], choices['computer'])
    print(result)

    options = input("Do You want play again [Y|N]")
    if options.lower()=='n':
        break

print()
print('Thanks! for playing this game....')
