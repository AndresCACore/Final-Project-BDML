import numpy as np
import cv2
import tensorflow as tf
from tf.keras.models import Model

IMG_SIZE = 145
def prepare(filepath, face_cas="Data/assets/haarcascade_frontalface_default.xml"):
    img_array = cv2.imread(filepath, cv2.IMREAD_COLOR)
    img_array = img_array / 255
    resized_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return resized_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)

model = tf.keras.models.load_model("Data/weight/drowiness_train.h5")

prediction = model.predict([prepare('Data/drowsiness-dataset/drowsy/10.jpg')])
np.argmax(prediction)