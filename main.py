__author__ = 'Shadow | shadowsgovernment.com'

from PySide.QtCore import *
from PySide.QtGui import *
from socket import *
import sys

import mainWindow

class MainDialog(QDialog, mainWindow.Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.btnScan, SIGNAL("clicked()"), self.scan)

    def scan(self):
        targetIP = gethostbyname(self.txtHost.text())
        self.txtLog.append('Starting scan on host %s' % targetIP)


        for i in range(int(self.txtBeginPort.text()), int(self.txtEndPort.text())):

            s = socket(AF_INET, SOCK_STREAM)

            result = s.connect_ex((targetIP, i))

            if result == 0:
                self.txtLog.append('Port %d OPEN' % i)
            s.close()
        self.txtLog.append('Scan Complete...')

app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
