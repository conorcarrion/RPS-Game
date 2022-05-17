import random
import time
#Intro
def battlecommences():
    print('PREPARE TO FIGHT! ')
    time.sleep(1)

#Bot and User choices    
def choices():
    global weapon
    weapon = ('rock', 'paper', 'scissors')
    global bot_choice
    bot_choice = random.choice(weapon)
    global user_choice
    user_choice = input('Select your weapon warrior: rock, paper or scissors! ')

#run countdown until show of hand
def countdown():
    print('Who wins this battle? ')
    count = 3
    while count >= 1:
        print(count)
        time.sleep(1)
        count = count - 1

#resolution of choices
def whowon():
    print(f'Bot chose {bot_choice}! ')
    if bot_choice == 'rock':
        if user_choice == 'paper':
            print('User won!')
            

        if user_choice == 'scissors':
            print('Bot won!')
            
        if user_choice == 'rock':
            print('It\'s a draw!')
            

    if bot_choice == 'paper':
        if user_choice == 'scissors':
            print('User won!')
            

        if user_choice == 'rock':
            print('Bot won!')
            
        if user_choice == 'paper':
            print('It\'s a draw!')
            

    if bot_choice == 'scissors':
        if user_choice == 'rock':
            print('User won!')
            

        if user_choice == 'paper':
            print('Bot won!')
            
        if user_choice == 'scissors':
            print('It\'s a draw!')
            
#sequence the program
def rockpaperscissors():
    battlecommences()
    choices()
    countdown()
    whowon()

#run the game
rockpaperscissors()
