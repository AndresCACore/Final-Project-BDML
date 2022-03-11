
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from out_window import Ui_OutputDialog

class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self._new_window = Ui_OutputDialog()
        self._new_window.show()
        #self._new_window.startVideo() # Choose the webcam

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    sys.exit(app.exec_())
