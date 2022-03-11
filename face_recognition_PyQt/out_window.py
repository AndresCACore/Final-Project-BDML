from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import cv2
import datetime
from face_recog import face_recog
import sys
from predict import predict

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

        drowsy_recognizer,imagePaths = predict()
            
        Capture = cv2.VideoCapture(0,cv2.CAP_DSHOW) #predict

            #predict
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
            #predict

        while self.ThreadActive: 
            ret, frame = Capture.read()
            if ret:
                    
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #gray

                    #predict
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                auxFrame = gray.copy()
                faces = faceClassif.detectMultiScale(gray,1.3,5)
                face_recog(faces, auxFrame, frame, drowsy_recognizer, imagePaths)

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


