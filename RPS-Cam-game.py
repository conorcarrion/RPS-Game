### Beginning of the Rock-Paper-Scissors code ###

# Imports
import cv2
from keras.models import load_model
import numpy as np
from numpy import argmax
import random
import time

# Camera and variable setup
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
botweapon = ['rock', 'paper', 'scissors']
userweapon = ['nothing','rock', 'paper', 'scissors']
user_score = 0
computer_score = 0
bot_choice = ''
user_choice = ''

# Function list

# Bot weapon
def get_computer_choice():
    bot_choice = random.choice(botweapon)
    return bot_choice

# Countdown
def countdown():
    print(f'Bot chose {bot_choice}! ')
    print('Who will emerge victorious? ')
    count = 3
    while count >= 1:
        print(count)
        time.sleep(1)
        count -= 1

def who_won_round():
    #decision making
    if bot_choice == 'rock':
        if user_choice == 'paper':
            user_score += 1
            print('User won! ')
            

        if user_choice == 'scissors':
            computer_score += 1
            print('Bot won! ')
            
        if user_choice == 'rock':
            print('It\'s a draw! ')
            

    if bot_choice == 'paper':
        if user_choice == 'scissors':
            user_score += 1
            print('User won! ')
            

        if user_choice == 'rock':
            computer_score += 1
            print('Bot won! ')
            
        if user_choice == 'paper':
            print('It\'s a draw! ')
            

    if bot_choice == 'scissors':
        if user_choice == 'rock':
            user_score += 1
            print('User won! ')
            

        if user_choice == 'paper':
            computer_score += 1
            print('Bot won! ')
            
        if user_choice == 'scissors':
            print('It\'s a draw! ')

    if user_choice == 'nothing ':
        computer_score += 1
        print('You failed to raise your weapon, you shameful coward! ')


def get_user_choice():
    user_choice = ''
    print('PREPARE TO FIGHT! DISPLAY YOUR WEAPON! PRESS \'Q\' TO FIGHT ')
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1
        # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)

        # fetch index of
        index = argmax(prediction)

        # print(prediction)
        
        if not user_choice == userweapon[index]:
            user_choice = userweapon[index]
            print(f'You wish to pick the {user_choice}?')

        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    print(f'You have chosen the way of the {user_choice}! ')          
    return 


    
    

def resolve_winner():
    if user_score == 2:
        print("User has won 2 rounds, they are declared winner!")

    if computer_score == 2:
        print("The Computer has won 2 rounds, they are declared winner!")

# Resolution
def play_a_round():
    get_computer_choice()
    get_user_choice()
    countdown()
    who_won_round()
    

def play():
        
    while user_score or computer_score <= 2:
        play_a_round()
    
    resolve_winner()
    
    return

play()
