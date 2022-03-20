import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QLabel
from PyQt5.uic import loadUi
import principal

class Login(QDialog):

    def __init__(self):
        super(Login,self).__init__()
        #Lance l'appli 
        loadUi("Le havre\Assets\main.ui",self)
        self.pushButton.clicked.connect(principal.building.importBuilding())

    def change(self):
        self.label_Argile.setText("test")


app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1080)
widget.setFixedHeight(620)
widget.show()
app.exec()