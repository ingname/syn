import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from auto.check_db import *
from des import *


class Interface(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.autores.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.login, self.ui.password]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)




    def check_input(funct):
        def wrapper(self):
            for login in self.base_line_edit:
                if len(login.text()) == 0:
                    return
            funct(self)
        return wrapper



    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)


    @check_input
    def auth(self):
        name = self.ui.login.text()
        passw = self.ui.password.text()
        self.check_db.thr_login(name, passw)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())

