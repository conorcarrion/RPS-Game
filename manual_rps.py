import random
import time

#Intro
def battlecommences():
    print('PREPARE TO FIGHT! ')
    time.sleep(1)

#Bot and User choices    
def get_user_choice():
    user_choice = input('Select your weapon warrior: rock, paper or scissors! ')
    return user_choice

def get_bot_choice():
    weapon = ('rock', 'paper', 'scissors')
    bot_choice = random.choice(weapon)
    return bot_choice

#run countdown until show of hand
def countdown():
    print('Who will win this battle? ')
    count = 3
    while count >= 1:
        print(count)
        time.sleep(1)
        count = count - 1

#resolution of choices
def get_winner(bot_choice, user_choice):
    print(f'Bot chose {bot_choice}! ')
    if bot_choice == 'rock':
        if user_choice == 'paper':
            print('User won!')
            

        if user_choice == 'scissors':
            print('Bot won!')
            
        if user_choice == 'rock':
            print('It\'s a draw!')
            

    elif bot_choice == 'paper':
        if user_choice == 'scissors':
            print('User won!')
            

        if user_choice == 'rock':
            print('Bot won!')
            
        if user_choice == 'paper':
            print('It\'s a draw!')
            

    elif bot_choice == 'scissors':
        if user_choice == 'rock':
            print('User won!')
            

        if user_choice == 'paper':
            print('Bot won!')
            
        if user_choice == 'scissors':
            print('It\'s a draw!')
    else:
        print('You raised an invalid weapon, you shameful coward!')

#sequence the program
def play():
    battlecommences()
    bot_choice = get_bot_choice()
    user_choice = get_user_choice()
    countdown()
    get_winner(bot_choice, user_choice)

#run the game
play()
