import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from homeControl_ui import *
import parser
from functools import partial
class HCMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(HCMainWindow,self).__init__(parent)        
        self.setupUi(self)
        
        self.pushButton_study_light_onfull.clicked.connect(partial(self.mainParser,'study-SC-study_light_on')) #书房灯全开
        self.pushButton_study_light_onhalf.clicked.connect(partial(self.mainParser,'study-SC-study_light_onhalf')) #书房灯半开
        self.pushButton_study_light_onmin.clicked.connect(partial(self.mainParser,'study-SC-study_light_onmin'))#书房灯微光
        self.pushButton_study_light_brighter.clicked.connect(partial(self.mainParser,'study-SC-study_light_brighter'))#书房灯增亮
        self.pushButton_study_light_dimmer.clicked.connect(partial(self.mainParser,'study-SC-study_light_dimmer'))#书房灯变暗
        self.pushButton_study_light_off.clicked.connect(partial(self.mainParser,'study-SC-study_light_off'))#书房灯关闭

        self.pushButton_study_AC_cool26.clicked.connect(partial(self.mainParser,'study-SC-study_AC_cool26'))#书房空调26度制冷
        self.pushButton_study_AC_off.clicked.connect(partial(self.mainParser,'study-SC-study_AC_off'))#书房空调关


        
    
    def mainParser(self,instruct):
        parser.parser(instruct)
        return True


if __name__=='__main__':
    app=QApplication(sys.argv)
    myWin = HCMainWindow()
    myWin.show()
    sys.exit(app.exec_())