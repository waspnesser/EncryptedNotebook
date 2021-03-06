from entrance import passwordEnter
from PyQt5.QtWidgets import QWidget,QLineEdit,QVBoxLayout,QHBoxLayout,QApplication,QPushButton,QLabel,QFileDialog
from PyQt5.QtCore import Qt
from functions import loadSystemInfo
from PyQt5.QtGui import QIcon

from specialWidgets import HoverButton

class optionPage(QWidget):
    def __init__(self):
        super(optionPage,self).__init__()

        self.systemInfo = loadSystemInfo()
        self.resulation = (self.systemInfo["width"],self.systemInfo["height"])
        self.setStyleSheet("background-color:#221515;")
        self.setWindowTitle("Encrypted Notebook")
        self.setGeometry(self.resulation[0]//2-175,self.resulation[1]//2-38,350,76)
        self.initUI()
    
    def initUI(self):
        self.verticalLay = QVBoxLayout()
        self.setMouseTracking(True)

        self.label = QLabel("Options")
        self.label.setStyleSheet("background-color:#bab5ae;font-family:'NewRocker';font-size:32px;font-weight:bold;color:  #3c1515;width:160px;height:30px;border-radius:3px;")
        self.label.setFixedHeight(64)
        self.label.setFixedWidth(240)

        button_enterSS = "background-color: #c7c3be;font-family:'NewRocker';font-size:16px;font-weight:bold;color:#4E4343;width:160px;height:30px;border-radius:3px;"
        button_leaveSS = "background-color: #bab5ae;font-family:'NewRocker';font-size:16px;font-weight:bold;color:#4E4343;width:160px;height:30px;border-radius:3px;"

        self.newFile = HoverButton("New Empty File",button_enterSS,button_leaveSS)
        self.newFile.setFixedHeight(32)
        self.newFile.setFixedWidth(160)
        self.newFile.clicked.connect(self.newFileFunction)

        self.loadNew = HoverButton("Load A New File",button_enterSS,button_leaveSS)
        self.loadNew.setFixedHeight(32)
        self.loadNew.setFixedWidth(160)
        self.loadNew.clicked.connect(self.loadNewFunction)

        self.enterNormal = HoverButton("Open Loaded File",button_enterSS,button_leaveSS)
        self.enterNormal.setFixedHeight(32)
        self.enterNormal.setFixedWidth(160)
        self.enterNormal.clicked.connect(self.enterNormalFunction)
        
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)#Alignment
        self.verticalLay.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)#Alignment
        
        self.verticalLay.addWidget(self.label,alignment = Qt.AlignHCenter | Qt.AlignVCenter)
        self.verticalLay.addWidget(self.newFile,alignment = Qt.AlignHCenter | Qt.AlignVCenter)
        self.verticalLay.addWidget(self.loadNew,alignment = Qt.AlignHCenter | Qt.AlignVCenter)
        self.verticalLay.addWidget(self.enterNormal,alignment = Qt.AlignHCenter | Qt.AlignVCenter)
        self.setLayout(self.verticalLay)

    def enterNormalFunction(self):
    	self.pop = passwordEnter(option = 1)
    	self.pop.show()
    	self.close()

    def newFileFunction(self):
    	self.pop = passwordEnter(option = 2)
    	self.pop.show()
    	self.close()    	

    def loadNewFunction(self):
        fileName = QFileDialog.getOpenFileName(self, 'OpenFile')
        path = fileName[0]# Not checked is it text or not
        self.pop = passwordEnter(option = 3,pathForNewOne = path)
        self.pop.show()
        self.close()

if __name__ == "__main__":
    import sys,os
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(loadSystemInfo()["path"]+"Staff{}encrypt.png".format(os.sep)))
    window = optionPage()
    window.show()
    app.exec()          	