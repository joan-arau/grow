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

from scipy.interpolate import griddata
import numpy as np



from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure



import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('QT5Agg')
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')


# path = os.path.dirname(__file__) #uic paths from itself, not the active dir, so path needed
qtCreatorFile = "/Users/joan/PycharmProjects/grow/plot_ui.ui" #Ui file name, from QtDesigner, assumes in same folder as this .py

SB_Output, QtBaseClass = uic.loadUiType(qtCreatorFile) #process through pyuic




class MyApp1(QMainWindow,  SB_Output): #gui class
    def __init__(self,parms):
        #The following sets up the gui via Qt
        super(MyApp1, self).__init__()

        self.setupUi(self)
        names = {'hum':'Humidity %','temp':'Temperature C','moist':'Soil Moisture %'}

        self.data = parms[0][['time',parms[1]]]
        self.name = names[parms[1]]
        print(self.name,self.data)
        self.label.setText(self.name)

        # self.label.setText(str(parms[-4]))
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)

        #
        # ax = self.canvas.figure.add_subplot(111)
        # self.canvas.figure.tight_layout()
        # ax.clear()
        # ax.plot(self.output[0]['spot'],self.output[0]['pnl'])
        # self.canvas.figure.style.use('dark_background')
        # self.canvas.draw()







        # fig = plt.figure()
        # ax = fig.add_subplot(111, projection='3d')
        # %matplotlib


        # surf = ax.plot_wireframe(x2, y2, z2, rstride=1, cstride=1)

        date_axis = pg.graphicsItems.DateAxisItem.DateAxisItem(orientation='bottom')
        self.graphWidget = pg.PlotWidget(axisItems={'bottom': date_axis})

        self.gridLayout.addWidget(self.graphWidget,0,0)



        self.data['rolling'] = self.data[parms[1]].rolling(30).mean()
        self.data = self.data.dropna().reset_index(drop=True)
        print(self.data)

        self.graphWidget.plot(self.data['time'].values.astype(np.int64) // 10 ** 9,self.data['rolling'])

        self.graphWidget.sizeHint = lambda: pg.QtCore.QSize(100, 100)

        self.graphWidget.showGrid(x=True, y=True)












        self.b_close.clicked.connect(self.close)


        self.setStyleSheet(qdarkstyle.load_stylesheet())









def plot_Ui(parms):
    # app = QApplication(sys.argv) #instantiate a QtGui (holder for the app)


    global window
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = MyApp1(parms)
    window.show()
    # sys.exit(app.exec_())
    return window

if __name__ == "__main__":
    plot_Ui()