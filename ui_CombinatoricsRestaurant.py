from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math






class Ui_MainWindow(object):

    def plot(self):
        plt.plot(self.x,self.y)
        plt.draw()
        plt.show()
                

    def combinatorics(self):
        app = len(self.AppeBox.toPlainText().split('\n'))
        ent = len(self.EntrBox.toPlainText().split('\n'))
        des = len(self.DessBox.toPlainText().split('\n'))
        dri = len(self.DrinBox.toPlainText().split('\n'))

        count = app + ent + des + dri
        combinations = app*ent*des*dri

        self.total.setText('Total combinations: '+str(combinations))
        if (self.x[-1] != count and self.y[-1]!= combinations):
            self.x.append(count)
            self.y.append(combinations)
                    
            
    def erase(self):
        self.AppeBox.setText('')
        self.EntrBox.setText('')
        self.DessBox.setText('')
        self.DrinBox.setText('')

        self.total.setText('Total Combinations: 0')

        self.x = [0]
        self.y = [0]

        #clear map and value
        
    #############################
    def setupUi(self, MainWindow):
        self.x = [0]
        self.y = [0]

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")


        self.Combinatorics = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.Combinatorics.setFont(font)
        self.Combinatorics.setObjectName("Combinatorics")
        self.gridLayout_2.addWidget(self.Combinatorics, 0, 0, 1, 3)


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1)
        self.pushButton.clicked.connect(lambda: self.erase())


        self.Appetizers = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Appetizers.setFont(font)
        self.Appetizers.setObjectName("Appetizers")
        self.gridLayout_2.addWidget(self.Appetizers, 1, 0, 1, 1)


        self.AppeBox = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AppeBox.setFont(font)
        self.AppeBox.setObjectName("AppeBox")
        self.gridLayout_2.addWidget(self.AppeBox, 2, 0, 1, 1)
        self.AppeBox.textChanged.connect(lambda: self.combinatorics())
        

        self.Entrees = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Entrees.setFont(font)
        self.Entrees.setObjectName("Entrees")
        self.gridLayout_2.addWidget(self.Entrees, 1, 1, 1, 1)


        self.EntrBox = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EntrBox.setFont(font)
        self.EntrBox.setObjectName("EntrBox")
        self.gridLayout_2.addWidget(self.EntrBox, 2, 1, 1, 1)
        self.EntrBox.textChanged.connect(lambda: self.combinatorics())


        self.Desserts = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Desserts.setFont(font)
        self.Desserts.setObjectName("Desserts")
        self.gridLayout_2.addWidget(self.Desserts, 1, 2, 1, 1)


        self.DessBox = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DessBox.setFont(font)
        self.DessBox.setObjectName("DessBox")
        self.gridLayout_2.addWidget(self.DessBox, 2, 2, 1, 1)
        self.DessBox.textChanged.connect(lambda: self.combinatorics())


        self.Drinks = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Drinks.setFont(font)
        self.Drinks.setObjectName("Drinks")
        self.gridLayout_2.addWidget(self.Drinks, 1, 3, 1, 1)


        self.DrinBox = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DrinBox.setFont(font)
        self.DrinBox.setObjectName("DrinBox")
        self.gridLayout_2.addWidget(self.DrinBox, 2, 3, 1, 1)
        self.DrinBox.textChanged.connect(lambda:self.combinatorics())

        self.Plotbtn = QtWidgets.QPushButton(self.centralwidget)
        self.Plotbtn.setObjectName("Plotbtn")
        self.gridLayout_2.addWidget(self.Plotbtn, 3, 2, 1, 1)
        self.Plotbtn.clicked.connect(lambda: self.plot())


        self.total = QtWidgets.QLabel(self.centralwidget)
        self.total.setObjectName("total")
        self.gridLayout_2.addWidget(self.total, 3, 3, 1, 1)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Entrees.setText(_translate("MainWindow", "Entrees"))
        self.Appetizers.setText(_translate("MainWindow", "Appetizers"))
        self.pushButton.setText(_translate("MainWindow", "Clear Menu"))
        self.Desserts.setText(_translate("MainWindow", "Desserts"))
        self.Drinks.setText(_translate("MainWindow", "Drinks"))
        self.Plotbtn.setText(_translate("MainWindow", "Plot"))
        self.total.setText(_translate("MainWindow", "Total Combinations: 0"))
        self.Combinatorics.setText(_translate("MainWindow", "The Cheesecake Factory"))
        self.AppeBox.setText("Calamari \nFried Mozzarella")
        self.EntrBox.setText("Chicken Alfredo \nShrimp Carbonara")
        self.DessBox.setText("Tiramisu")
        self.DrinBox.setText("Water")
        


if __name__ == "__main__": #### Creates Scene ####
    import sys
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    comb = QMainWindow()
    ui.setupUi(comb)
    comb.show()
    sys.exit(app.exec())
