from cgitb import reset
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from PySide2 import QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(284, 215)
        self.counterFlag = 0
        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(40, 50, 181, 51))
        self.incBtn = QPushButton(Form)
        self.incBtn.setObjectName(u"incBtn")
        self.incBtn.setGeometry(QRect(20, 130, 101, 25))
        self.decBtn = QPushButton(Form)
        self.decBtn.setObjectName(u"decBtn")
        self.decBtn.setGeometry(QRect(168, 130, 91, 25))
        self.resetBtn = QPushButton(Form)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setGeometry(QRect(100, 180, 89, 25))
        self.resetBtn.clicked.connect(lambda:self.reset())
        self.incBtn.clicked.connect(lambda:self.increment())
        self.decBtn.clicked.connect(lambda:self.decrement())
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def increment(self):
        self.counterFlag+=1
        self.lcdNumber.display(self.counterFlag)
        
    def decrement(self):
        if self.counterFlag<=0:
            self.showdialog()
            return
        self.counterFlag -=1
        self.lcdNumber.display(self.counterFlag)
        
    def reset(self):
        self.counterFlag = 0
        self.lcdNumber.display(self.counterFlag)
    
    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Negative number")
        msg.setInformativeText("Value cannot be less then zero!")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Counter", None))
        self.incBtn.setText(QCoreApplication.translate("Form", u"+", None))
        self.decBtn.setText(QCoreApplication.translate("Form", u"-", None))
        self.resetBtn.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    widget = Ui_Form()
    widget.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
