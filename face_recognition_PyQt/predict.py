import cv2
import tensorflow as tf
# Prepare the img
IMG_SIZE = 145
def prepare(filepath, face_cas="Data/assets/modeloLBPH.xmñ"):
    img_array = cv2.imread(filepath, cv2.IMREAD_COLOR)
    img_array = img_array / 255
    resized_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return resized_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)

# Predict model
def predict():
    method = 'LBPH'
    if method == 'LBPH': drowsy_recognizer = cv2.face.LBPHFaceRecognizer_create()
    drowsy_recognizer.read('modelo'+method+'.xml')
    imagePaths= ['alert', 'drowsy', 'no_yawn', 'yawn']
    print('imagePaths=',imagePaths)
    
    #model = tf.keras.models.load_model("Final-Project-BDML/Data/weight/drowiness_train.h5")
    #prediction = model.predict([prepare(frame)]) #frame
    #pred = imagePaths[np.argmax(prediction)]
    #print(pred)
    

    return drowsy_recognizer,imagePaths









