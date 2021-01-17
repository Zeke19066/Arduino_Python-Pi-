"""
Garden Station.py UI v1.0

Needed:
    - Initialize with spalsh screen
    - Upgrade timing function
    - Use QTextEdit for splash screen notes
    - Store QSettings for Common Names & Taxonomy
    - Impliment Update Button functionality
"""
import numpy
import sys
import os
import time
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import Garden_Station_Arduino as Arduino

title_style = QtGui.QFont('Trebuchet MS', 30)
mini_style = QtGui.QFont('Trebuchet MS', 9)
mini_style.setItalic(1)
custom_style1 = QtGui.QFont('Trebuchet MS', 16)
custom_style2 = QtGui.QFont('Trebuchet MS', 12)
custom_style2.setItalic(1)
custom_style3 = QtGui.QFont('Trebuchet MS', 16)


class Garden_Station(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #Arduino.update_values()
        layout = QGridLayout()
        layout.addWidget(self.title_module(), 0, 0, 2, 20)  
        layout.addWidget(self.sensor_module(1), 5, 0, 1, 10) #(row, column, hight, width)
        layout.addWidget(self.sensor_module(2), 6, 0, 1, 10)
        layout.addWidget(self.sensor_module(3), 7, 0, 1, 10)
        layout.addWidget(self.sensor_module(4), 5, 10, 1, 10)
        layout.addWidget(self.sensor_module(5), 6, 10, 1, 10)
        layout.addWidget(self.sensor_module(6), 7, 10, 1, 10)   
        layout.addWidget(self.new_button("update_button"), 12, 0, 1, 20)
        layout.addWidget(self.new_button("quit_button"), 13, 0, 1, 20)   
        self.setLayout(layout)
        launchcode(self)
    
    def sensor_module(self, sensor_number):

        if sensor_number == 1:
            pbarVal = int(map(Arduino.average(Arduino.readout1)))
            rawVal = int(Arduino.average(Arduino.readout1))
        elif sensor_number == 2:
            pbarVal = int(map(Arduino.average(Arduino.readout2)))
            rawVal = int(Arduino.average(Arduino.readout2))
        elif sensor_number == 3:
            pbarVal = int(map(Arduino.average(Arduino.readout3)))
            rawVal = int(Arduino.average(Arduino.readout3))
        elif sensor_number == 4:
            pbarVal = int(map(Arduino.average(Arduino.readout4)))
            rawVal = int(Arduino.average(Arduino.readout4))
        elif sensor_number == 5:
            pbarVal = int(map(Arduino.average(Arduino.readout5)))
            rawVal = int(Arduino.average(Arduino.readout5))
        else:
            pbarVal = 50
            rawVal = "Error"

        groupbox = QGroupBox()
        
        pbar = QProgressBar(self)
        pbar.setFont(QtGui.QFont('Trebuchet MS', 10))
        if int(pbarVal) < 50:
            pbar.setStyleSheet(pbar_Style1)
        else:
            pbar.setStyleSheet(pbar_Style2)
        pbar.setValue(pbarVal) 
        sensor = QLabel(f"S{sensor_number}")
        sensor.setAlignment(Qt.AlignCenter)
        sensor.setFont(custom_style2)
        sensor.setStyleSheet("""
            border :8px solid black;
            border-color: rgb(40,44,52);
            background-color: rgb(209,154,102);
            color: rgb(40,44,52);
            border-radius: 12px;
            """)
        raw = QLabel('Raw:', self)
        raw.setText(f"Raw: {rawVal}")
        raw.setFont(mini_style)
        raw.setStyleSheet("""
            border-color: rgb(152,195,121);
            color: rgb(152,195,121);
            border-width : 0px;
            border-style:inset;
            """)
        avg = QLabel('3DayAvg', self)
        avg.setText("3 Day Avg: 68%")
        avg.setFont(mini_style)
        avg.setStyleSheet("""
            border-color: rgb(152,195,121);
            color: rgb(152,195,121);
            border-width : 0px;
            border-style:inset;
            """)
        plant = QLineEdit(
            "Western Swordfern",
            self,
            placeholderText = "Common Name"
            )
        plant.setFont(custom_style1)       
        plant.setStyleSheet("""
        border-color: rgb(40,44,52);
        color: white;
        border-width : 0px;
        border-style:inset;
        """)
        planttaxon = QLineEdit(
            "Polystichum munitum",
            self,
            placeholderText = "Taxonomy"
            )
        planttaxon.setFont(custom_style2)
        planttaxon.setStyleSheet("""
        border-color: rgb(40,44,52);
        color: rgb(80,167,239);
        border-width : 0px;
        border-style:inset;
        """)

        gridsensor = QGridLayout()
        gridsensor.addWidget(pbar,1,0,1,2)
        gridsensor.addWidget(raw,2,1)
        gridsensor.addWidget(avg,2,0)
        gridsensor.addWidget(plant,3,0)
        gridsensor.addWidget(sensor,3,1)
        gridsensor.addWidget(planttaxon,4,0)
        groupbox.setLayout(gridsensor)
        groupbox.setFont(custom_style2)
        groupbox.setStyleSheet("""
                QGroupBox {
                    border :3px solid black;
                    border-color: rgb(255,255,255);
                    color: rgb(209,154,102);
                    border-radius: 8px;
                    border-width : 4px;
                    }
            """)
        return groupbox

    def title_module(self):
        titlebox = QGroupBox("")
        titlebox.setStyleSheet("""
            border-color: rgb(255,255,255);
            color: rgb(255,255,255);
            border-radius: 8px;
            border-width : 4px;
            border-style:outset;
            """)
        titlebar = QLabel('GardenStation', self)
        titlebar.setText("Garden Station")
        titlebar.setFont(title_style)
        titlebar.setStyleSheet("color: rgb(255,255,255);border-width : 0px;")
        subtitlebar = QLabel('v1.0 Beta', self)
        subtitlebar.setFont(custom_style2)
        subtitlebar.setStyleSheet("color: rgb(80,167,239);border-width : 0px;")
        titlegrid = QGridLayout()
        titlegrid.addWidget(titlebar, 4, 0)
        titlegrid.addWidget(subtitlebar, 6, 0)
        titlebox.setLayout(titlegrid)
        return titlebox

    def new_button(self, button_request):
        if button_request == "update_button":
            update_btn = QPushButton('Update', self)
            update_btn.setFont(custom_style3)
            update_btn.setStyleSheet("""
            border-color: rgb(255,255,255);
            color: rgb(255,255,255);
            border-radius: 8px;
            border-width : 4px;
            border-style:outset;
            """)
            update_btn.clicked.connect(self.buttonClicked)
            return update_btn

        elif button_request == "quit_button":
            qbtn = QPushButton('Quit', self)
            qbtn.setFont(custom_style3)
            qbtn.setStyleSheet("""
            border-color: rgb(255,255,255);
            color: rgb(255,255,255);
            border-radius: 8px;
            border-width : 4px;
            border-style:outset;
            """)
            qbtn.clicked.connect(QApplication.instance().quit)
            return qbtn

    def buttonClicked(self):
        restart_program()

#margin: 1px;   <- under chunk
pbar_Style1 = """
QProgressBar{
    border: 4px solid grey;
    border-radius: 5px;
    border-color: rgb(152,195,121);
    color: rgb(152,195,121);
    text-align: center
}
QProgressBar::chunk {
    background-color: rgb(152,195,121);
    width: 10px;
}
"""
pbar_Style2 = """
QProgressBar{
    border: 4px solid grey;
    border-radius: 5px;
    border-color: rgb(152,195,121);
    color: rgb(40,44,52);
    text-align: center
}
QProgressBar::chunk {
    background-color: rgb(152,195,121);
    width: 10px;
}
"""

def map(x):
    result = ((x-1028)*(100-0)/(430-1028) + 0)
    return result

def launchcode(self):      #the universal 'show' protocol 
    self.setGeometry(500, 500, 3000, 700)
    self.setStyleSheet("background-color: rgb(40,44,52);")
    self.setWindowTitle('Garden Station')
    self.show()

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def main():
    app = QApplication(sys.argv)
    ex = Garden_Station()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()