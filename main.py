from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pyTzoker import *
import sys
import random
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #setup btnCalculate
        self.ui.btnCalculate.clicked.connect(self.onCalculate)

        #setup vars
        self.random5 = []

    def onCalculate(self):
        #reset list
        self.random5.clear()

        while len(self.random5) < 5:
            # get a random number
            n = self.GetNumber()
            #append number to list
            self.random5.append(n)
            #create a unique number list
            myset = set(self.random5)
            self.random5 = list(myset)
            self.random5.sort()

        #Get Tzoker number
        tzoker = self.GetTzoker()

        #Print the output
        sOutput = "Οι τυχεροί αριθμοί του ΤΖΟΚΕΡ είναι: "

        #Get 5 numbers from list
        for i in self.random5:
            sOutput = sOutput + str(i) + " "

        #get tzoker
        sOutput = sOutput + "\nΚαι ο αριθμός ΤΖΟΚΕΡ είναι το " + str(tzoker)

        #Fill txtOutput
        self.ui.txtOutput.setPlainText(sOutput)

    def GetNumber(self):
        random.seed(datetime.now().timestamp())
        number = random.randint(1, 45)
        return number

    def GetTzoker(self):
        random.seed(datetime.now().timestamp())
        number = random.randint(1, 20)
        return number


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    #   Disable maximize window button
    w.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
    w.show()
    sys.exit(app.exec_())