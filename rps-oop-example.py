### Beginning of the Rock-Paper-Scissors code ###

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import random
import time

import cv2
import numpy as np
from keras.models import load_model

# Camera and model setup
model = load_model("keras_model.h5")
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


# Rock Paper Scissor class with methods
class Player:
    weapons = ["rock", "paper", "scissors"]

    def __init__(self):
        self.score = 0

    def choose_weapon(self):
        pass


class Bot(Player):
    def choose_weapon(self):
        return random.choice(self.weapons)

    def __str__(self):
        return "Bot"


class User(Player):
    weapons = ["nothing", "rock", "paper", "scissors"]

    def __init__(self, name="You"):
        super().__init__()
        self.name = name

    # User gets ~3 seconds to display gesture
    def choose_weapon(self):
        round_time = time.time()

        run = True
        while run:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1

            # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data, verbose=0)
            cv2.imshow("frame", frame)
            # cv2.waitKey(1)

            index = np.argmax(prediction)

            # Close after 6 seconds (3 sec startup, 3 sec to display)
            if time.time() > round_time + 6:
                break

        return self.weapons[index]

    def __str__(self):
        return self.name


class Rps:

    choice_map = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
        "nothing": None,
    }

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        print("Welcome to Rock, Paper, Scissors by Conor Quinn!")
        time.sleep(1)
        while not (self.player1.score == 2 or self.player2.score == 2):
            winner = self.fight()
            if winner:
                print(f"{winner} won!")
                winner.score += 1
            time.sleep(2)
            print(
                f"{self.player1} - {self.player1.score}, {self.player2.score} - {self.player2}"
            )

        self.resolve_match_winner()
        time.sleep(2)
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        print("ggwp, re? ")

    # Compare choices, return winner
    def fight(self):
        print("A new round has started!")
        print("PREPARE TO FIGHT! DISPLAY YOUR WEAPONS! ")

        weapon1 = self.player1.choose_weapon()
        weapon2 = self.player2.choose_weapon()

        print(f"{self.player1} has chosen the way of the {weapon1}! ")
        print(f"{self.player2} has chosen the way of the {weapon2}! ")

        if weapon1 == "nothing":
            print(f"{self.player1} failed to raise your weapon, you shameful coward! ")
            return self.player2

        elif weapon2 == "nothing":
            print(f"{self.player2} failed to raise your weapon, you shameful coward! ")
            return self.player1

        elif self.choice_map[weapon1] == weapon2:
            return self.player1

        elif self.choice_map[weapon2] == weapon1:
            return self.player2

        else:
            print("It's a draw! ")
            return None

    # The player with the higest score is the winner
    def resolve_match_winner(self):
        winner = (
            self.player1 if self.player1.score > self.player2.score else self.player2
        )
        print(f"{winner} won 2 rounds, they are the winner! ")


game = Rps(User("Conor"), Bot())
game.play()
