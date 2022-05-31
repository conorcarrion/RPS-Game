# Rock Paper Scissors ReadMe

## Milestone 1: Create the model

I used '[Teachable Machine](https://teachablemachine.withgoogle.com/)', a machine learning tool, to create a model for the game 'Rock, Paper Scissors'. 'Teachable Machine' is a web-based tool that allows creation of machine learning models through a simple GUI (graphical user interface). In the tool I created 4 classes of response: 'Nothing', 'Rock', 'Paper' and 'Scissors'. By using a webcam and positioning my hand, I captured 200 shots of each of the poses symbolising those 4 classes. While taking the 200 shots I moved my hand and body to introduce some noise into the model to reduce overfitting. I also took shots in a medium light setting. 

I will use this trained model to create a Rock-Paper-Scissors game, playable by the user with a webcam against a random response generated computer opponent.

## Milestone 2: Install the dependencies

I set up my virtual environment with conda, running python 3.8 in vscode. I imported the libraries required: opencv, tensorflow and ipykernel. 

Using code to run the opencv library provided by the AIcore team, I tested my Teachable Machine model to ensure the gestures I made were being recognised by the model and output by the prediction function.

```
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
```

This code uses opencv (open computer vision) for the webcam input, tensorflow (keras) for interpretation of the teachable machine model and numpy to create an array with the image. 
print(prediction) prints a list(?) of the models certainty that the current webcam input matches either of the 4 gestures it was trained on: 

```
Nothing	Rock		Paper		Scissors
[[1.6709046e-05 3.2001196e-07 1.0888249e-06 9.9998188e-01]]
```
(labels not present in the terminal, added here for clarity)

In the case above I was raising the scissors gesture, and the prediction is 9.9998188 out of 10 certain that I am displaying the scissors gesture. By testing this on all 4 gestures I was able to see that my model was correctly predicting the gesture I was showing it.

## Milestone 3: Create a Rock-Paper-Scissors game

I used Python3 to code a game of Rock-Paper-Scissors. I split the program into 4 components: the announcement of the start of the battle, an input for the user to choose their weapon, an exciting countdown followed by resolution of the choices to decide the victor. I used an explicit series of 'if' statements to resolve the game. While not concise, this presents little ambiguity in the program's execution and provides legibility for future changes.

The only input required is the user's choice which they type into the terminal in response to the input() function.

## Milestone 4 - Use the camera to play Rock-Paper-Scissors

I integrated my teachable machine model into my Rock-Paper-Scissors (RPS) game, using the camera input and OpenCV to see my gesture and tensorflow with the teachable machine model to predict my gesture. I then used numpy's argmax to convert the model prediction output into a string describing my gesture eg. scissors. I then integrated that into my `get_user_choice()` function. I then reworked the game to run multiple rounds, keeping score of those rounds and declaring a winner when a player has won 2 rounds.

An initial challenge was coding the RPS game around the While loop which runs the camera interface. How should the user choice be made? After a certain period of time or by pressing a button? Should the output be a snapshot of the final prediction or the most common prediction from a recorded list?

I decided to simply use a timer and a snapshot method for simplicity and because I felt my model was accurate and reliable. I tried various methods to run the entire game inside the 'While loop' creating the camera output but I struggled to do this for multiple rounds of the game. I put the 'while loop' controlling the camera into the `get_user_choice()` function so that the game only runs the while loop for 6 seconds to get a snapshot of the user choice. The image freezes between rounds.

I faced many problems with the architecture of the program: partially from not understanding what certain provided parts did, partially from not fully understanding any particular programming paradigm. 

I had import and library issues with virtual environments and branches. My attempts to remove debugging information created issues of their own. 

This was my first time creating a program from scratch without detailed step by step guidance, as well as my first time setting up ubuntu dual boot, vscode, pip & conda, using virtual environments, git, github and using the terminal. 







