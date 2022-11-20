from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def login(self, login, passw, signal):
        con = sqlite3.connect('auto/users.db')
        cur = con.cursor()

        cur.execute(f'SELECT * FROM users WHERE login="{login}";')
        value = cur.fetchall()

        if value != [] and value[0][2] == passw:
            return 1
        else:
            signal.emit('Проверьте правильность ввода данных!')

        cur.close()
        con.close()

    def thr_login(self, name, passw):
        self.login(name, passw, self.mysignal)