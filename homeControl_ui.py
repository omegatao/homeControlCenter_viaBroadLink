# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeControl_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 753)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 70, 601, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 591, 261))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_study_light_onfull = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_study_light_onfull.setGeometry(QtCore.QRect(10, 30, 81, 211))
        font = QtGui.QFont()
        font.setFamily("文泉驿等宽微米黑")
        font.setPointSize(15)
        self.pushButton_study_light_onfull.setFont(font)
        self.pushButton_study_light_onfull.setObjectName("pushButton_study_light_onfull")
        self.pushButton_study_light_onhalf = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_study_light_onhalf.setGeometry(QtCore.QRect(110, 30, 81, 211))
        font = QtGui.QFont()
        font.setFamily("文泉驿等宽微米黑")
        font.setPointSize(15)
        self.pushButton_study_light_onhalf.setFont(font)
        self.pushButton_study_light_onhalf.setObjectName("pushButton_study_light_onhalf")
        self.pushButton_study_light_onmin = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_study_light_onmin.setGeometry(QtCore.QRect(220, 30, 81, 211))
        font = QtGui.QFont()
        font.setFamily("文泉驿等宽微米黑")
        font.setPointSize(15)
        self.pushButton_study_light_onmin.setFont(font)
        self.pushButton_study_light_onmin.setObjectName("pushButton_study_light_onmin")
        self.pushButton_study_light_off = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_study_light_off.setGeometry(QtCore.QRect(500, 30, 81, 211))
        font = QtGui.QFont()
        font.setFamily("文泉驿等宽微米黑")
        font.setPointSize(15)
        self.pushButton_study_light_off.setFont(font)
        self.pushButton_study_light_off.setObjectName("pushButton_study_light_off")
        self.pushButton_study_light_brighter = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_study_light_brighter.setGeometry(QtCore.QRect(330, 60, 131, 51))
        font = QtGui.QFont()
        font.setFamily("文泉驿等宽微米黑")
        font.setPointSize(12)
        self.pushButton_study_light_brighter.setFont(font)
        self.pushButton_study_light_brighter.setObjectName("pushButton_study_light_brighter")
        self.pushButton_study_light_dimmer = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_study_light_dimmer.setGeometry(QtCore.QRect(330, 120, 131, 51))
        font = QtGui.QFont()
        font.setFamily("文泉驿等宽微米黑")
        font.setPointSize(12)
        self.pushButton_study_light_dimmer.setFont(font)
        self.pushButton_study_light_dimmer.setObjectName("pushButton_study_light_dimmer")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 280, 591, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 30, 81, 211))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HomeControl设备控制中心"))
        self.label.setText(_translate("MainWindow", "家庭设备控制中心"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "客厅"))
        self.groupBox.setTitle(_translate("MainWindow", "主灯"))
        self.pushButton_study_light_onfull.setText(_translate("MainWindow", "全开"))
        self.pushButton_study_light_onhalf.setText(_translate("MainWindow", "半开"))
        self.pushButton_study_light_onmin.setText(_translate("MainWindow", "微光"))
        self.pushButton_study_light_off.setText(_translate("MainWindow", "关灯"))
        self.pushButton_study_light_brighter.setText(_translate("MainWindow", "亮度增加"))
        self.pushButton_study_light_dimmer.setText(_translate("MainWindow", "亮度降低"))
        self.groupBox_2.setTitle(_translate("MainWindow", "空调"))
        self.pushButton_8.setText(_translate("MainWindow", "夏季制冷26℃"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "书房"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "主卧"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "次卧"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "厨房"))

