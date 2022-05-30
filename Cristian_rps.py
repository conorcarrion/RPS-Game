
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import random
import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')

class rps:
    def __init__(self, option_list) -> None:
        self.computer_choice = random.choice(option_list)
        self.computer_score = 0
        self.user_score = 0
        pass

    def get_computer_choice(self):
        return(self.computer_choice)

    def get_prediction(self):
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        flag = False
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data, verbose=0)
            cv2.imshow('video', frame)
            # Press q to close the window 
            
            if cv2.waitKey(1) & 0xFF == ord('g'):
                flag = True
                start = time.time()
            if flag == True:
                end = 5 - (time.time() - start)
                current_score = "You: " + str(self.user_score), "Computer: " + str(self.computer_score)
                cv2.putText(frame, str(int(end)), (350,238), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 3, cv2.LINE_4)
                cv2.putText(frame, str(current_score), (31,445), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3, cv2.LINE_4)
                cv2.imshow('frame', frame)
                if end <= 0:
                    print(prediction)
                    if prediction[0][0] > 0.5:
                        user_choice ="Rock"
                    elif prediction[0][1] > 0.5:
                        user_choice ="Paper"
                    elif prediction[0][2] > 0.5:
                        user_choice = "Scissors"
                    elif prediction[0][3] > 0.5:
                        flag = False
                        continue
                    break
            else:
                continue 
        cap.release()
        cv2.destroyAllWindows()
        rps.get_winner(self, user_choice)
      
    def get_user_choice(self):

        user_choice = input("Choose Rock, Paper or Scissors: ")

        while True:
            if user_choice in option_list:
                rps.get_winner(self, user_choice)
                break
            else:
                print("Please enter either Rock, Paper or Scissors")
            break  
        pass
            
    def get_winner(self, user_choice):
        if self.computer_choice == user_choice:
            print("It's a draw")
        else:
            if self.computer_choice == "Rock":
                if user_choice == "Paper":
                    print("You win a point!")
                    print("The computer chose", self.computer_choice)
                    self.user_score += 1
                    print("You: ", self.user_score, "Computer: ", self.computer_score)
                else:
                    print("You lost, the computer gets a point")
                    print("The computer chose", self.computer_choice)
                    self.computer_score += 1
                    print("You: ", self.user_score, "Computer: ", self.computer_score)
                
            elif self.computer_choice == "Paper":
                if user_choice == "Scissors":
                    print("You win a point!")
                    print("The computer chose", self.computer_choice)
                    self.user_score += 1
                    print("You: ", self.user_score, "Computer: ", self.computer_score)
                else: 
                    print("You lost, the computer gets a point")
                    print("The computer chose", self.computer_choice)
                    self.computer_score += 1
                    print("You: ", self.user_score, "Computer: ", self.computer_score)

            elif self.computer_choice == "Scissors":
                if user_choice == "Rock":
                    print("You win a point!")
                    print("The computer chose", self.computer_choice)
                    self.user_score += 1
                    print("You: ", self.user_score, "Computer: ", self.computer_score)
                else:
                    print("You lost, the computer gets a point")
                    print("The computer chose", self.computer_choice)
                    self.computer_score += 1
                    print("You: ", self.user_score, "Computer: ", self.computer_score)
        pass

def play(option_list):
    game = rps(option_list)

    while True:
        game.get_prediction()
        if game.computer_score == 3:
            print("The computer has won the game! Better luck next time.")
            break
        elif game.user_score == 3:
            print("You have won the game! Congratulations")
            break
        else:
            continue
    
if __name__ == '__main__':
    option_list = ["Rock", "Paper", "Scissors"]
    play(option_list)