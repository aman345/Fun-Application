from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar
import sys
import time
import psutil


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        #MainWindow.resize(269, 390)
        MainWindow.setFixedSize(269,390)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.cpu = QFrame(self.centralwidget)
        self.cpu.setObjectName(u"cpu")
        self.cpu.setGeometry(QRect(10, 30, 251, 91))
        self.cpu.setFrameShape(QFrame.StyledPanel)
        self.cpu.setFrameShadow(QFrame.Raised)
        self.ram = QFrame(self.centralwidget)
        self.ram.setObjectName(u"ram")
        self.ram.setGeometry(QRect(10, 150, 251, 101))
        self.ram.setFrameShape(QFrame.StyledPanel)
        self.ram.setFrameShadow(QFrame.Raised)
        self.gpu = QFrame(self.centralwidget)
        self.gpu.setObjectName(u"gpu")
        self.gpu.setGeometry(QRect(10, 280, 251, 101))
        self.gpu.setFrameShape(QFrame.StyledPanel)
        self.gpu.setFrameShadow(QFrame.Raised)
        self.cpul = QLabel(self.centralwidget)
        self.cpul.setObjectName(u"cpul")
        self.cpul.setGeometry(QRect(10, 10, 81, 17))
        self.labelraml_2 = QLabel(self.centralwidget)
        self.labelraml_2.setObjectName(u"labelraml_2")
        self.labelraml_2.setGeometry(QRect(10, 130, 91, 17))
        self.gpul = QLabel(self.centralwidget)
        self.gpul.setObjectName(u"gpul")
        self.gpul.setGeometry(QRect(10, 260, 81, 17))
        MainWindow.setCentralWidget(self.centralwidget)
        #progress bar  ram
        self.round_progress_bar_ram = roundProgressBar()
        self.round_progress_bar_ram.rpb_setMaximum(100)
        self.round_progress_bar_ram.rpb_setBarStyle('Line')
        self.round_progress_bar_ram.rpb_setInitialPos('West')
        self.layout_ram = QHBoxLayout(self.ram)
        self.layout_ram.addWidget(QLabel("Ram :"))
        self.layout_ram.addWidget(self.round_progress_bar_ram)
        # progress bar cpu
        self.round_progress_bar_cpu = roundProgressBar()
        self.round_progress_bar_cpu.rpb_setMaximum(100)
        self.round_progress_bar_cpu.rpb_setBarStyle('Line')
        self.round_progress_bar_cpu.rpb_setInitialPos('West') 
        self.layout_cpu = QHBoxLayout(self.cpu)
        self.layout_cpu.addWidget(QLabel("CPU"))
        self.layout_cpu.addWidget(self.round_progress_bar_cpu)
        #progress bar gpu 
        self.round_progress_bar_gpu = roundProgressBar()
        self.round_progress_bar_gpu.rpb_setMaximum(100)
        self.round_progress_bar_gpu.rpb_setBarStyle('Line')
        self.round_progress_bar_gpu.rpb_setInitialPos('West')
        self.layout_gpu = QHBoxLayout(self.gpu)
        self.layout_gpu.addWidget(QLabel("GPU"))
        self.layout_gpu.addWidget(self.round_progress_bar_gpu)

        #############Threads class#######################
        #cpu threadclass
        self.cpuThread = ThreadClass(MainWindow)
        self.cpuThread.start()
        self.cpuThread.updateCpu.connect(self.updateCPUProgress)

        #ram threadclass
        self.ramThread = ThreadRam(MainWindow)
        self.ramThread.start()
        self.ramThread.updateRam.connect(self.updateRamProgress)

        #gpu threadclass

        self.gpuThread = ThreadGpu()
        self.gpuThread.start()
        self.gpuThread.gpuProgress.connect(self.updateGpuProgress)


        self.retranslateUi(MainWindow)
        #embedding the progress bar in frames
        

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(qtTrId(u"Load FIdget"))
        self.cpul.setText(qtTrId(u"Cpu Usage"))
        self.labelraml_2.setText(qtTrId(u"Ram Usage"))
        self.gpul.setText(qtTrId(u"Gpu Usage"))
    # retranslateUi
    #driver function for progress bar
    def updateCPUProgress(self,val):
        if val<=30:
            self.round_progress_bar_cpu.rpb_setLineColor((102,205,0))
        if val>30 and val<80:
            self.round_progress_bar_cpu.rpb_setLineColor((255,20,147))
        if val>=80:
            self.round_progress_bar_cpu.rpb_setLineColor((205,38,38))
        self.round_progress_bar_cpu.rpb_setValue(val)

    def updateRamProgress(self,val):
        if val<=30:
            self.round_progress_bar_ram.rpb_setLineColor((102,205,0))
        if val>30 and val<80:
            self.round_progress_bar_ram.rpb_setLineColor((255,69,0))
            #self.round_progress_bar_ram.rpb_setCircleColor((255,69,0))
        if val>=80:
            self.round_progress_bar_ram.rpb_setLineColor((205,38,38))
        self.round_progress_bar_ram.rpb_setValue(val) 

    def updateGpuProgress(self,val):
        self.round_progress_bar_gpu.rpb_setValue(val)    

class ThreadClass(QtCore.QThread):
    updateCpu =  QtCore.Signal(float)
    def __init__(self, pp):
        super(ThreadClass,self).__init__(pp)
    
    #run function of thread cycle
    def run(self):
       
        while 1:
            val = psutil.cpu_percent(interval=1)
            #for emiting the signal  for the application
            time.sleep(0.2)
            self.updateCpu.emit(val)

class ThreadRam(QtCore.QThread):
    updateRam =  QtCore.Signal(float)
    def __init__(self, pp):
        super(ThreadRam,self).__init__(pp)

    def run(self):
        while 1:
            value = psutil.virtual_memory().percent
            time.sleep(0.2)
            self.updateRam.emit(value)

class ThreadGpu(QtCore.QThread):
    gpuProgress = QtCore.Signal(float)
    def __init_(self,pp):
        super(ThreadClass.self).__init__(pp)
    
    def run(self):
        while 1:
            value =60
            time.sleep(0.2)
            self.gpuProgress.emit(value)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle("Usage Grabber")
    MainWindow.setStyleSheet("")
    widget = Ui_MainWindow()
    widget.setupUi(MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())
