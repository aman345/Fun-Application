from pickle import NONE
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets

import sys
import requests
import urllib.request

class Ui_Form(object):
    APP_KEY = ""
    def __init__(self,key,MainWindow):
        self.APP_KEY = key
        self.setupUi(MainWindow)
        self.updateWeather()

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setFixedSize(414, 241)
        Form.setStyleSheet(u"border-width: 2px;\n"
                           "border-radius: 10px;\n"
                           "border-color: beige;\n"
                           "background-color:white;\n"
                           "")
        self.openGLWidget = QLabel(Form)
        self.openGLWidget.setObjectName(u"openGLWidget")
        self.openGLWidget.setGeometry(QRect(10, 70, 186, 81))
        self.City = QLabel(Form)
        self.City.setObjectName(u"City")
        self.City.setGeometry(QRect(120, 70, 200, 100))
        self.Current_temperature = QLabel(Form)
        self.Current_temperature.setObjectName(u"Current_temperature")
        self.Current_temperature.setGeometry(QRect(10, 170, 186, 17))
        self.CurrTemp = QLabel(Form)
        self.CurrTemp.setObjectName(u"CurrTemp")
        self.CurrTemp.setGeometry(QRect(10, 200, 31, 17))
        self.search_temp = QPushButton(Form)
        self.search_temp.setObjectName(u"search_temp")
        self.search_temp.setGeometry(QRect(300, 20, 101, 31))
        self.search_temp.setStyleSheet(u"border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 10px;\n"
                                       "border-color: beige;\n"
                                       "font: bold 14px;\n"
                                       "padding: 6px;")
        self.city_input = QPlainTextEdit(Form)
        self.city_input.setObjectName(u"city_input")
        self.city_input.setGeometry(QRect(10, 20, 271, 31))
        self.city_input.setStyleSheet(u"border-style: outset;\n"
                                      "    border-width: 2px;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: beige;\n"
                                      "    font: bold 14px;\n"
                                      "    min-width: 10em;\n"
                                      "  ")
        self.search_temp.clicked.connect(lambda:self.updateWeather())
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    #weather updater
    def updateWeather(self):
        city = self.city_input.toPlainText() if self.city_input.toPlainText() !='' else 'Your Default city'
        baseurl = 'http://api.weatherapi.com/v1/current.json?key='+self.APP_KEY+'&q='+city+'&aqi=yes'
        res = requests.get(baseurl).json()
        self.City.setText(res['location']['name']+","+res['location']['region'])
        self.CurrTemp.setText(str(res['current']["temp_c"]))
        data = urllib.request.urlopen("http:"+res['current']['condition']['icon']).read()
        image = QImage()
        image.loadFromData(data)
        self.openGLWidget.setPixmap(QPixmap(image))
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Weather Widget", None))
        self.City.setText(QCoreApplication.translate("Form", u"--", None))
        self.Current_temperature.setText(
            QCoreApplication.translate("Form", u"Current Temperature", None))
        self.CurrTemp.setText(QCoreApplication.translate(
            "Form", u"<html><head/><body><p><span style=\" font-weight:600;\">--</span></p></body></html>", None))
        self.search_temp.setText(
            QCoreApplication.translate("Form", u"Search", None))
    # retranslateUi
if __name__ == "__main__":
    api_key = 'your_api_key_weather_api key'
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    widget = Ui_Form(api_key,MainWindow)
    #widget.setupUi(MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())
