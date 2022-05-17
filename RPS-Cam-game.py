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


# Function list

# Bot weapon
def get_bot_choice():
    bot_choice = random.choice(botweapon)
    return bot_choice

# Countdown
def countdown():
    print('Who has emerged victorious? ')
    count = 3
    while count >= 1:
        print(count)
        
        count -= 1

def get_user_choice(prediction):
    
    print('PREPARE TO FIGHT! DISPLAY YOUR WEAPON! ')
    
    # fetch weapon from prediction
    index = argmax(prediction)
    user_choice = userweapon[index]
     

        
    print(f'You have chosen the way of the {user_choice}! ')          
    return user_choice

def who_won_round(bot_choice, user_choice, user_score, bot_score):
    #decision making
    print(f'Bot chose {bot_choice}! ')
    if bot_choice == 'rock':
        if user_choice == 'paper':
            user_score += 1
            print('You won! ')
            

        if user_choice == 'scissors':
            bot_score += 1
            print('Bot won! ')
            
        if user_choice == 'rock':
            print('It\'s a draw! ')
            

    if bot_choice == 'paper':
        if user_choice == 'scissors':
            user_score += 1
            print('You won! ')
            

        if user_choice == 'rock':
            bot_score += 1
            print('Bot won! ')
            
        if user_choice == 'paper':
            print('It\'s a draw! ')
            

    if bot_choice == 'scissors':
        if user_choice == 'rock':
            user_score += 1
            print('You won! ')
            

        if user_choice == 'paper':
            bot_score += 1
            print('Bot won! ')
            
        if user_choice == 'scissors':
            print('It\'s a draw! ')

    if user_choice == 'nothing':
        bot_score += 1
        print('You failed to raise your weapon, you shameful coward! ')
    return user_score, bot_score

def resolve_winner(user_score, bot_score):
    if user_score == 2:
        print("You have won 2 rounds, you are the winner! ")

    if bot_score == 2:
        print("Bot has won 2 rounds, you lose! ")

def match_end():
    print("ggwp, re? ")
    

# Resolution
def play_a_round(prediction):
    user1 = get_user_choice(prediction)
    bot1 = get_bot_choice()
    countdown()
    user_score, bot_score = who_won_round(bot1, user1)
    return user_score, bot_score
    
def play():
   
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1
        
        # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        
        # Time to make gesture
        cam_start = time.time()
              
        if time.time() > cam_start + 5:
            user_score, bot_score = play_a_round(prediction)

        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   

        if user_score or bot_score == 2:
            break
    return user_score, bot_score
    
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    resolve_winner(user_score, bot_score)
    match_end()
    
play()
