import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from homeControl_ui import *
import parser
from functools import partial
class HCMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(HCMainWindow,self).__init__(parent)        
        self.setupUi(self)
        
        self.pushButton_study_light_onfull.clicked.connect(partial(self.mainParser,'study-SC-study_light_onfull'))
        self.pushButton_study_light_onhalf.clicked.connect(partial(self.mainParser,'study-SC-study_light_on')) 
        self.pushButton_study_light_onmin.clicked.connect(partial(self.mainParser,'study-SC-study_light_ondim'))
        self.pushButton_study_light_brighter.clicked.connect(partial(self.mainParser,'study-SC-study_light_brighter'))
        self.pushButton_study_light_dimmer.clicked.connect(partial(self.mainParser,'study-SC-study_light_dimmer'))        

        
    
    def mainParser(self,instruct):
        parser.parser(instruct)
        return True


if __name__=='__main__':
    app=QApplication(sys.argv)
    myWin = HCMainWindow()
    myWin.show()
    sys.exit(app.exec_())