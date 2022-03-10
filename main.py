import numpy as np
import tensorflow as tf
from predict import prepare

# Predict model

model = tf.keras.models.load_model("Data/weight/drowiness_train.h5")
prediction = model.predict([prepare('Data/drowsiness-dataset/drowsy/10.jpg')]) #frame
labels = ['yawn', 'no_yawn', 'alert', 'drowsy']
pred = labels[np.argmax(prediction)]
print(pred)

