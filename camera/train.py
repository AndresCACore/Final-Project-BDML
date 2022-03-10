import cv2
import os
import numpy as np
import time


def obtenerModelo(method,facesData,labels):
	#if method == 'EigenFaces': drowsy_recognizer = cv2.face.EigenFaceRecognizer_create()
	#if method == 'FisherFaces': drowsy_recognizer = cv2.face.FisherFaceRecognizer_create()
	if method == 'LBPH': drowsy_recognizer = cv2.face.LBPHFaceRecognizer_create()

	print("Entrenando ( "+method+" )...")
	inicio = time.time()
	drowsy_recognizer.train(facesData, np.array(labels))
	tiempoEntrenamiento = time.time()-inicio
	print("Tiempo de entrenamiento ( "+method+" ): ", tiempoEntrenamiento)

	drowsy_recognizer.write("modelo"+method+".xml")

dataPath = 'drowsiness-dataset/train' 
drowsyList = os.listdir(dataPath)
print('labels: ', drowsyList)

labels = []
facesData = []
label = 0

for nameDir in drowsyList:
	drowsyPath = dataPath + '/' + nameDir

	for fileName in os.listdir(drowsyPath):
		labels.append(label)
		facesData.append(cv2.imread(drowsyPath+'/'+fileName,0))

	label = label + 1

#obtenerModelo('EigenFaces',facesData,labels)
#obtenerModelo('FisherFaces',facesData,labels)
obtenerModelo('LBPH',facesData,labels)