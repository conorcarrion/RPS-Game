# Rock Paper Scissors ReadMe

## Milestone 1: Create the model

I used '[Teachable Machine](https://teachablemachine.withgoogle.com/)', a machine learning tool, to create a model for the game 'Rock, Paper Scissors'. 'Teachable Machine' is a web-based tool that allows creation of machine learning models through a simple GUI (graphical user interface). In the tool I created 4 classes of response: 'Nothing', 'Rock', 'Paper' and 'Scissors'. By using a webcam and positioning my hand, I captured 200 shots of each of the poses symbolising those 4 classes. While taking the 200 shots I moved my hand and body to introduce some noise into the model to reduce overfitting. I also took shots in a medium light setting. 

I will use this trained model to create a Rock-Paper-Scissors game, playable by the user with a webcam against a random response generated computer opponent.

## Milestone 2: Install the dependencies

I set up my virtual environment with conda, running python 3.8 in vscode. I imported the libraries required: opencv, tensorflow and ipykernel. 

Using code to run the opencv library provided by the AIcore team, I tested my Teachable Machine model to ensure the gestures I made were being recognised by the model and output by the prediction function.

'''python
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
'''

This code uses opencv (open computer vision) for the webcam input, tensorflow (keras) for interpretation of the teachable machine model and numpy to create an array with the image. 
print(prediction) prints a list(?) of the models certainty that the current webcam input matches either of the 4 gestures it was trained on: 

'''bash
Nothing	Rock		Paper		Scissors
[[1.6709046e-05 3.2001196e-07 1.0888249e-06 9.9998188e-01]]
'''
(labels not present in the terminal, added here for clarity)

In the case above I was raising the scissors gesture, and the prediction is 9.9998188 out of 10 certain that I am displaying the scissors gesture. By testing this on all 4 gestures I was able to see that my model was correctly predicting the gesture I was showing it.

## Milestone 3: Create a Rock-Paper-Scissors game

I used Python3 to code a game of Rock-Paper-Scissors. I split the program into 4 components: the announcement of the start of the battle, an input for the user to choose their weapon, an exciting countdown followed by resolution of the choices to decide the victor. I used an explicit series of 'if' statements to resolve the game. While not concise, this presents little ambiguity in the program's execution and provides legibility for future changes.

'''python
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
'''

'''bash
(camera_rps) ../Rock Paper Scissors$ python3 manual_rps.py 
PREPARE TO FIGHT! 
Select your weapon warrior: rock, paper or scissors! rock
Who will win this battle? 
3
2
1
Bot chose scissors! 
User won!
'''
The input 'rock' was typed into the terminal in response to the input() function.

## Milestone 4 - Use the camera to play Rock-Paper-Scissors

I integrated my teachable machine model into my Rock-Paper-Scissors (RPS) game. I faced several challenges getting it to work how I wanted. 

An initial challenge was coding the RPS game around the While loop which runs the camera interface. How should the user choice be made? After a certain period of time or by pressing a button? Should the output be a snapshot of the final prediction or the most common prediction from a recorded list?

I decided to simply use a timer and a snapshot method for simplicity and because I felt my model was accurate and reliable. I tried various methods to run the entire game inside the While loop creating the camera output but I struggled to do this for multiple rounds of the game. Later on I found this was probably due to my misplacement of:

'''python
# After the loop release the cap object 
    cap.release()
    # Destroy all the windows (there's only 1)
    cv2.destroyAllWindows()
 '''
 ... which I should have placed at the end of the match instead.
 
So I put the while loop controlling the camera into the get_user_choice() function so that the game only runs the while loop for 6 seconds to get a snapshot of the user choice. The image freezes between rounds.

I faced many problems with the logic of the code, partially from not understanding what certain provided parts did, partially from import issues and library issues with virtual environments. My attempts to remove debugging information created issues of their own. 

This was not just my first time creating a program from scratch without excess specific guidance, but also setting up ubuntu dual boot, vscode, pip & conda, using virtual environments, git, github, command line / bash. 

My version of Rock-Paper-Scissors is fairly straight forward. Now I have better understanding of certain parts, I believe I could re-write it to keep the webcam input active the entire match. I could then add text to the image showing the score and various game messages instead of in the terminal. However I do feel the terminal adds some 90s charm to the game. I also would have to use time.time() instead of time.sleep() to create pauses in the game flow. 








