### Beginning of the Rock-Paper-Scissors code ###

# Imports
import cv2
import os
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
weaponguess = []
bot_choice = ''
user_choice = ''
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# Function list

# Weapon counter
def most_frequent(list):
    counter = 0
    num = list[0]
    for i in list:
        curr_frequency = list.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

# Countdown
def countdown():
    print('Who wins this battle? ')
    time.sleep(3)

# Resolution
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
    if user_choice == 'nothing':
        print('You failed to raise your weapon, you shameful coward!')

# Begin fight, initialise camera
print('PREPARE TO FIGHT! DISPLAY YOUR WEAPON! PRESS \'Q\' TO FIGHT')
while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1
    # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)

    # Model prediction into class
    index = argmax(prediction)

    # print(prediction)
    print(userweapon[index])

    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

# Set choices
bot_choice = random.choice(botweapon)
user_choice = userweapon[index]
print(f'You have chosen the way of the {user_choice}! ')          

countdown()
whowon()

