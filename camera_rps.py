### Beginning of the Rock-Paper-Scissors code ###

# Imports
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import cv2
from keras.models import load_model
import numpy as np
import random
import time


# Camera and variable setup
model = load_model('keras_model.h5')

cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
botweapon = ['rock', 'paper', 'scissors']
userweapon = ['nothing', 'rock', 'paper', 'scissors']


# Function list

# Bot weapon
def get_bot_choice():
    bot_choice = random.choice(botweapon)
    return bot_choice

# User gets ~3 seconds to display gesture 
def get_user_choice():
    round_time = time.time()
    
    print('PREPARE TO FIGHT! DISPLAY YOUR WEAPON! ')
    
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1
        
        # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data, verbose=0)
        cv2.imshow('frame', frame)

        index = np.argmax(prediction)
        user_choice = userweapon[index]
               
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   
        # Close after 6 seconds (3 sec startup, 3 sec to display)
        if time.time() > round_time + 6:
            break
             
    print(f'You have chosen the way of the {user_choice}! ')          
    return user_choice
    
    
# Takes the user and bot choices, decides who won and adds the outcome to the score
def who_won_round(bot_choice, user_choice):
    #decision making
    print(f'Bot chose {bot_choice}! ')
    if bot_choice == 'rock':
        if user_choice == 'paper':
            print('You won! ')
            return 'user'

        if user_choice == 'scissors':
            print('Bot won! ')
            return 'bot'
            
        if user_choice == 'rock':
            print('It\'s a draw! ')
            return 'draw'
            

    if bot_choice == 'paper':
        if user_choice == 'scissors':
            print('You won! ')
            return 'user'
            

        if user_choice == 'rock':
            print('Bot won! ')
            return 'bot'
            
        if user_choice == 'paper':
            print('It\'s a draw! ')
            return 'draw'
            

    if bot_choice == 'scissors':
        if user_choice == 'rock':
            print('You won! ')
            return 'user'
            

        if user_choice == 'paper':
            print('Bot won! ')
            return 'bot'
            
        if user_choice == 'scissors':
            print('It\'s a draw! ')
            return 'draw'

    if user_choice == 'nothing':
        print('You failed to raise your weapon, you shameful coward! ')
        return 'bot'
 
# Flow of a round
def play_a_round():
    print('A new round has started!' )
    time.sleep(1)
    user_choice = get_user_choice()
    bot_choice = get_bot_choice()
    time.sleep(1)
    result = who_won_round(bot_choice, user_choice)
    return result

# Run the match    
def play():
    user_score = 0
    bot_score = 0
    print('Welcome to Rock, Paper, Scissors by Conor Quinn!')
    time.sleep(1)
    while not (user_score == 2 or bot_score == 2):
        result = play_a_round()
        if result == 'user':
            user_score += 1

        if result == 'bot':
            bot_score += 1
        
    if user_score == 2:
        print("You have won 2 rounds, you are the winner! ")

    if bot_score == 2:
        print("Bot has won 2 rounds, you lose! ")
    
    time.sleep(2)
    # After the loop release the cap object 
    cap.release()
    # Destroy all the windows 
    cv2.destroyAllWindows()
    print('ggwp, re?')
    
play()
