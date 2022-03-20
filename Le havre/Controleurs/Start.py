import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):

    def __init__(self):
        super(Login,self).__init__()
        #Lance l'appli 
        loadUi("Le havre\Assets\start.ui",self)
        self.button_Start.clicked.connect(self.Message)

    def Message(self):
        print("test")


app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1080)
widget.setFixedHeight(620)
widget.show()
app.exec()