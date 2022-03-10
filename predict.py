import cv2
# Prepare the img
IMG_SIZE = 145
def prepare(filepath, face_cas="Data/assets/modeloLBPH.xmñ"):
    img_array = cv2.imread(filepath, cv2.IMREAD_COLOR)
    img_array = img_array / 255
    resized_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return resized_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)

