import cv2
import os
from keras.models import load_model
import numpy as np
from numpy import argmax
list = ['nothing', 'rock', 'paper', 'scissors']

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    index = argmax(prediction)
    print(list[index])

    cv2.imshow('frame', frame)
    # Press q to close the window
    # print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
