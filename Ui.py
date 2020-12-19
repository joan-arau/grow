import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from  get_files import get_temp
from configparser import ConfigParser
from os import listdir
from os.path import isfile, join
from datetime import datetime
import pandas as pd
from plot_ui import plot_Ui
temp = '/Users/joan/PycharmProjects/grow/temp/'
# path = os.path.dirname(__file__) #uic paths from itself, not the active dir, so path needed
qtCreatorFile = "/Users/joan/PycharmProjects/grow/ui.ui" #Ui file name, from QtDesigner, assumes in same folder as this .py

Ui_Settings, QtBaseClass = uic.loadUiType(qtCreatorFile) #process through pyuic

class MyApp1(QMainWindow, Ui_Settings): #gui class
    def __init__(self):
        try:
            get_temp()
        except:
            pass
        super(MyApp1, self).__init__()
        self.setupUi(self)
        self.df = pd.read_csv('/Users/joan/PycharmProjects/grow/temp/data.csv')[['hum', 'moist', 'temp', 'time']]
        self.df['time'] = pd.to_datetime(self.df['time'], format='%m%d%Y%H%M%S')
        self.df['hum'] = self.df['hum'] *0.55 #- 30
        self.df['temp'] = self.df['temp'] -1  # - 30
        print(self.df)
        last_row=list(self.df.iterrows())[-1]

        self.b_hum.setText('Humidity: '+str(round(float(last_row[1]['hum'])))+'%')
        self.b_hum.clicked.connect(lambda: self.create_plot('hum'))
        self.b_temp.setText('Temperature: ' + str(round(float(last_row[1]['temp']))) + 'C')
        self.b_temp.clicked.connect(lambda: self.create_plot('temp'))
        self.b_moist.setText('Soil Moisture: ' + str(round(float(last_row[1]['moist']))) + '%')
        self.b_moist.clicked.connect(lambda: self.create_plot('moist'))

        self.temp_files = [f for f in listdir(temp) if isfile(join(temp, f))]
        self.img = 0
        #The following sets up the gui via Qt




        self.resize(1000,800)


        # self.port_in.setText(config.get('main', 'ibkr_port'))
        self.label.resize(self.width(), self.height())

        self.set_recent()
        #
        # pixmap = QtGui.QPixmap(temp +"12162020171326.jpg")
        #

        # self.label.setPixmap(pixmap.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))



        #set up callbacks

        self.b_close.clicked.connect(self.close)

        self.label.stackUnder(self.b_close)

        self.b_back.clicked.connect(self.change_pic)
        self.b_fwd.clicked.connect(self.change_fwd)


        self.setStyleSheet(qdarkstyle.load_stylesheet())
        # self.horizontalLayout.setStackingMode(QStackedLayout.StackAll)



    def set_recent(self):

        self.img=-1
        l = []
        for x in self.temp_files:

            # print(x,x[-4:])
            if x[-4:] == '.jpg':
                l.append(int(x[:-4]))

        img = temp + str(sorted(l)[-1]) + '.jpg'
        pixmap = QtGui.QPixmap(img)
        # print(img)
        self.label.setPixmap(pixmap.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))
        current_time = str(datetime.strptime(str(sorted(l)[self.img]), "%m%d%Y%H%M%S"))
        self.label_2.setText(current_time)


    def change_pic(self):


            # print(onlyfiles)
        l = []
        for x in self.temp_files:


            # print(x,x[-4:])
            if x[-4:] == '.jpg':
                l.append(int(x[:-4]))


            # print(sorted(l))

        try:
            self.img -= 1
            img = temp + str(sorted(l)[self.img]) +'.jpg'

            pixmap = QtGui.QPixmap(img)
            # print(img)
            self.label.setPixmap(pixmap.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))
            current_time = str(datetime.strptime(str(sorted(l)[self.img]), "%m%d%Y%H%M%S"))
            self.label_2.setText(current_time)
        except:
            pass







    def change_fwd(self):



        # print(onlyfiles)
        l = []
        for x in self.temp_files:


            # print(x,x[-4:])
            if x[-4:] == '.jpg':
                l.append(int(x[:-4]))


        # print(sorted(l))
        if self.img != -1:
            self.img += 1
            img = temp + str(sorted(l)[self.img]) +'.jpg'

            pixmap = QtGui.QPixmap(img)
            # print(img)
            self.label.setPixmap(pixmap.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))
            current_time = str(datetime.strptime(str(sorted(l)[self.img]), "%m%d%Y%H%M%S"))
            self.label_2.setText(current_time)

    def create_plot(self,dt):

        print(dt)
        plot_Ui([self.df,dt])






def settingsGUI():
    app = QApplication(sys.argv) #instantiate a QtGui (holder for the app)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = MyApp1()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    settingsGUI()