from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import cv2
import datetime
from recorder import recorder
import sys

class Ui_OutputDialog(QDialog):
    def __init__(self):
        super(Ui_OutputDialog, self).__init__()
        loadUi("./outputwindow.ui", self)

        #Update time
        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.Date_Label.setText(current_date)
        self.Time_Label.setText(current_time)
        #self.StatusLabel.setText("Danger")

        self.image = None

        #predict

        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()
        #predict

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        
        self.ThreadActive = True

        # predict
        method = 'LBPH'
        if method == 'LBPH': drowsy_recognizer = cv2.face.LBPHFaceRecognizer_create()
        drowsy_recognizer.read('modelo'+method+'.xml')
        imagePaths= ['alert', 'drowsy', 'no_yawn', 'yawn']
        print('imagePaths=',imagePaths)
            #predict

            #Capture = cv2.VideoCapture(0) #original
        Capture = cv2.VideoCapture(0,cv2.CAP_DSHOW) #predict

            #precit
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
            #precit

        while self.ThreadActive: 
            ret, frame = Capture.read()
            if ret:
                    
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #gray

                    #predict
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                auxFrame = gray.copy()
                faces = faceClassif.detectMultiScale(gray,1.3,5)

                for (x,y,w,h) in faces:
                    rostro = auxFrame[y:y+h,x:x+w]
                    rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
                    result = drowsy_recognizer.predict(rostro)
                    cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
                     
                    if result[1] < 70:
                        cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                        #self.StatusLabel.setText(imagePaths[result[0]])
                        date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
                        recorder(date_time_string, imagePaths[result[0]])

                    else:
                        cv2.putText(frame,'No identificado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                    #predict

                    #FlippedImage = cv2.flip(frame, 1)
                FlippedImage = frame
                ConvertToQtFormat = QImage(FlippedImage, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                Pic= Pic.rgbSwapped()
                self.ImageUpdate.emit(Pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = Ui_OutputDialog()
    Root.show()
    sys.exit(App.exec())


