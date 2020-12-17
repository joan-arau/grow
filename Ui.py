import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import qdarkstyle
from pyqtgraph import PlotWidget, plot
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph.opengl as gl
from IPython.display import HTML, display
from scipy.interpolate import griddata
import numpy as np
import pandas as pd


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import webbrowser


from IPython.core.display import HTML
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('QT5Agg')




# path = os.path.dirname(__file__) #uic paths from itself, not the active dir, so path needed
qtCreatorFile = "/Users/joan/PycharmProjects/grow/Ui.ui" #Ui file name, from QtDesigner, assumes in same folder as this .py

ui, QtBaseClass = uic.loadUiType(qtCreatorFile) #process through pyuic


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self):

        super(MyApp1, self).__init__()





        self.setupUi(self)




class MyApp1(QMainWindow,  ui): #gui class


    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.initUI()

    def initUI(self):
        pass
        # self.resize(1000,600)
        # self.center()
        # self.setWindowTitle('Browser')
        #
        # self.lb = QLabel(self)
        # pixmap = QtGui.QPixmap("/Users/joan/PycharmProjects/grow/temp/12162020171326.jpg")
        # height_of_label = 100
        # self.lb.resize(self.width(), self.height())
        # self.lb.setPixmap(pixmap.scaled(self.lb.size(), QtCore.Qt.IgnoreAspectRatio))
        # self.show()

    def resizeEvent(self, event):

        pass
        # self.lb.resize(self.width(), self.lb.height())
        # self.lb.setPixmap(self.lb.pixmap().scaled(self.lb.size(), QtCore.Qt.IgnoreAspectRatio))
        # QWidget.resizeEvent(self, event)


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def grow_ui():
    app = QApplication(sys.argv) #instantiate a QtGui (holder for the app)


    # global window
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = MyApp1()
    window.show()
    sys.exit(app.exec_())
    # return window

if __name__ == "__main__":
    grow_ui()

# import sys
# from PyQt5 import QtGui,QtCore
#
# class PrettyWidget(QWidget):
#
#     def __init__(self, parent=None):
#         QWidget.__init__(self, parent=parent)
#         self.initUI()
#
#     def initUI(self):
#         self.resize(1000,600)
#         self.center()
#         self.setWindowTitle('Browser')
#
#         self.lb = QLabel(self)
#         pixmap = QtGui.QPixmap("/Users/joan/PycharmProjects/grow/temp/12162020171326.jpg")
#         height_of_label = 100
#         self.lb.resize(self.width(), self.height())
#         self.lb.setPixmap(pixmap.scaled(self.lb.size(), QtCore.Qt.IgnoreAspectRatio))
#         self.show()
#
#     def resizeEvent(self, event):
#         self.lb.resize(self.width(), self.lb.height())
#         self.lb.setPixmap(self.lb.pixmap().scaled(self.lb.size(), QtCore.Qt.IgnoreAspectRatio))
#         QWidget.resizeEvent(self, event)
#
#
#     def center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
# def main():
#     app = QApplication(sys.argv)
#     w = PrettyWidget()
#     app.exec_()
#
# main()