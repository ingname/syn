from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from threading import Timer
from datetime import datetime


class UiDialog(object):
    # Используется для создания метода, который ничего не знает о классе или экземпляре, через который он был вызван.
    @staticmethod
    def setupui(dialog):
        # Работа с окном
        dialog.setFixedSize(800, 500)
        palette = QtGui.QPalette()
        dialog.setPalette(palette)
        dialog.setWindowTitle("Syn")

         # Иннициализация обьектов выводимых на экран
    def __init__(self, dialog):
        # ----------------Надписи-----------------#

        # "Введите логин"
        self.text_enter_login = QtWidgets.QPushButton(dialog)
        self.text_enter_login.setGeometry(QtCore.QRect(150, 190, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_enter_login.setFont(font)
        self.text_enter_login.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # "Страница"
        self.text_stranica = QtWidgets.QPushButton(dialog)
        self.text_stranica.setGeometry(QtCore.QRect(180, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_stranica.setFont(font)
        self.text_stranica.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # "Такой страницы нет"
        self.text_takoi_str_net = QtWidgets.QPushButton(dialog)
        self.text_takoi_str_net.setGeometry(QtCore.QRect(200, 390, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_takoi_str_net.setFont(font)
        self.text_takoi_str_net.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # "Роль: "
        self.text_role = QtWidgets.QPushButton(dialog)
        self.text_role.setGeometry(QtCore.QRect(170, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_role.setFont(font)
        self.text_role.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # "login"
        self.text_login_login = QtWidgets.QPushButton(dialog)
        self.text_login_login.setGeometry(QtCore.QRect(240, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_login_login.setFont(font)
        self.text_login_login.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # "Admin"
        self.text_role_admin = QtWidgets.QPushButton(dialog)
        self.text_role_admin.setGeometry(QtCore.QRect(240, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_role_admin.setFont(font)
        self.text_role_admin.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # "Информация о пользоваетеле"
        self.text_about_us = QtWidgets.QPushButton(dialog)
        self.text_about_us.setGeometry(QtCore.QRect(180, 170, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_about_us.setFont(font)
        self.text_about_us.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Текст Пароль
        self.text_password = QtWidgets.QPushButton(dialog)
        self.text_password.setGeometry(QtCore.QRect(200, 180, 120, 30))
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_password.setFont(font)
        self.text_password.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Текст Вы ввели не правильные логин или пароль
        self.text_error_log = QtWidgets.QPushButton(dialog)
        self.text_error_log.setGeometry(QtCore.QRect(205, 300, 385, 30))
        font.setFamily("Candara Light")
        font.setPointSize(16)
        self.text_error_log.setFont(font)
        self.text_error_log.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Текст Логин
        self.text_login = QtWidgets.QPushButton(dialog)
        self.text_login.setGeometry(QtCore.QRect(200, 140, 120, 30))
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_login.setFont(font)
        self.text_login.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Текст входа
        self.text_vhod = QtWidgets.QPushButton(dialog)
        self.text_vhod.setGeometry(QtCore.QRect(250, 60, 300, 50))
        font.setFamily("Candara Light")
        font.setPointSize(35)
        self.text_vhod.setFont(font)
        self.text_vhod.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Текст ваши очки
        self.text_your_points = QtWidgets.QPushButton(dialog)
        self.text_your_points.setGeometry(QtCore.QRect(10, 40, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_your_points.setFont(font)
        self.text_your_points.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Текст очки
        self.text_points = QtWidgets.QPushButton(dialog)
        self.text_points.setGeometry(QtCore.QRect(20, 70, 81, 21))
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_points.setFont(font)
        self.text_points.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Текст Товары
        self.text_things = QtWidgets.QPushButton(dialog)
        self.text_things.setGeometry(QtCore.QRect(260, 90, 111, 31))
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_things.setFont(font)
        self.text_things.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Текст пользователи
        self.text_admin_users = QtWidgets.QPushButton(dialog)
        self.text_admin_users.setGeometry(QtCore.QRect(330, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_admin_users.setFont(font)
        self.text_admin_users.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        self.text_admin = QtWidgets.QPushButton(dialog)
        self.text_admin.setGeometry(QtCore.QRect(330, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_admin.setFont(font)
        self.text_admin.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        self.text_items = QtWidgets.QPushButton(dialog)
        self.text_items.setGeometry(QtCore.QRect(330, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_items.setFont(font)
        self.text_items.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # ----------------Кнопки-----------------#

        self.button_add_item_func = QtWidgets.QPushButton(dialog)
        self.button_add_item_func.setGeometry(QtCore.QRect(310, 400, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_add_item_func.setFont(font)

        # Кнопка добавить пользователя
        self.button_admin_add_user = QtWidgets.QPushButton(dialog)
        self.button_admin_add_user.setGeometry(QtCore.QRect(310, 160, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.button_admin_add_user.setFont(font)

        # Кнопка изменить доступ
        self.button_admin_access = QtWidgets.QPushButton(dialog)
        self.button_admin_access.setGeometry(QtCore.QRect(310, 220, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_admin_access.setFont(font)

        # Кнопка добавить баллы
        self.button_add_points = QtWidgets.QPushButton(dialog)
        self.button_add_points.setGeometry(QtCore.QRect(140, 320, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_add_points.setFont(font)

        # Кнопка снять баллы
        self.button_delete_points = QtWidgets.QPushButton(dialog)
        self.button_delete_points.setGeometry(QtCore.QRect(480, 320, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_delete_points.setFont(font)

        # Кнопка добавить предмет
        self.button_add_item = QtWidgets.QPushButton(dialog)
        self.button_add_item.setGeometry(QtCore.QRect(310, 160, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_add_item.setFont(font)

        # Кнопка удалить предмет
        self.button_delete_item = QtWidgets.QPushButton(dialog)
        self.button_delete_item.setGeometry(QtCore.QRect(310, 220, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_delete_item.setFont(font)

        # Кнопка изменить about us
        self.button_about_us_change = QtWidgets.QPushButton(dialog)
        self.button_about_us_change.setGeometry(QtCore.QRect(645, 400, 145, 40))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_about_us_change.setFont(font)

        # Кнопка админ изменение очков
        self.button_points_change = QtWidgets.QPushButton(dialog)
        self.button_points_change.setGeometry(QtCore.QRect(310, 160, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_points_change.setFont(font)

        # Кнопка админ изменение товаров
        self.button_things_change = QtWidgets.QPushButton(dialog)
        self.button_things_change.setGeometry(QtCore.QRect(310, 220, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_things_change.setFont(font)

        # Кнопка админ изменение пользователя
        self.button_users_change = QtWidgets.QPushButton(dialog)
        self.button_users_change.setGeometry(QtCore.QRect(310, 280, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_users_change.setFont(font)

        # Кнопка Начисление юзеру
        self.button_nachis_user = QtWidgets.QPushButton(dialog)
        self.button_nachis_user.setGeometry(QtCore.QRect(210, 270, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.button_nachis_user.setFont(font)

        # Кнопка Списание юзера
        self.button_spisania_user = QtWidgets.QPushButton(dialog)
        self.button_spisania_user.setGeometry(QtCore.QRect(370, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.button_spisania_user.setFont(font)

        # Кнопка Покупки юзера
        self.button_pokupki_user = QtWidgets.QPushButton(dialog)
        self.button_pokupki_user.setGeometry(QtCore.QRect(70, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.button_pokupki_user.setFont(font)

        # Кнопка Покупки
        self.button_shoping = QtWidgets.QPushButton(dialog)
        self.button_shoping.setGeometry(QtCore.QRect(10, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.button_shoping.setFont(font)

        # Кнопка Начисления баллов
        self.button_history_add_points = QtWidgets.QPushButton(dialog)
        self.button_history_add_points.setGeometry(QtCore.QRect(140, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.button_history_add_points.setFont(font)

        # Кнопка Списания
        self.button_spisania = QtWidgets.QPushButton(dialog)
        self.button_spisania.setGeometry(QtCore.QRect(290, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.button_spisania.setFont(font)

        # Кнопка История пользователя
        self.button_history_user = QtWidgets.QPushButton(dialog)
        self.button_history_user.setGeometry(QtCore.QRect(420, 90, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.button_history_user.setFont(font)

        # Кнопка изменить стр
        self.button_change_str = QtWidgets.QPushButton(dialog)
        self.button_change_str.setGeometry(QtCore.QRect(370, 430, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_change_str.setFont(font)

        # Кнопка Назад
        self.button_back = QtWidgets.QPushButton(dialog)
        self.button_back.setGeometry(QtCore.QRect(10, 50, 200, 40))
        font.setFamily("Candara Light")
        font.setPointSize(16)
        self.button_back.setFont(font)

        self.button_add_user_add = QtWidgets.QPushButton(dialog)
        self.button_add_user_add.setGeometry(QtCore.QRect(320, 320, 160, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_add_user_add.setFont(font)

        self.button_change_role = QtWidgets.QPushButton(dialog)
        self.button_change_role.setGeometry(QtCore.QRect(320, 320, 160, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_change_role.setFont(font)

        # Кнопка Входа
        self.button_entrance = QtWidgets.QPushButton(dialog)
        self.button_entrance.setGeometry(QtCore.QRect(300, 250, 200, 40))
        font.setFamily("Candara Light")
        font.setPointSize(16)
        self.button_entrance.setFont(font)

        # Кнопка Главная
        self.button_main = QtWidgets.QPushButton(dialog)
        self.button_main.setGeometry(QtCore.QRect(0, 0, 161, 31))
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_main.setFont(font)

        # Кнопка Личный кабинет
        self.button_your_cab = QtWidgets.QPushButton(dialog)
        self.button_your_cab.setGeometry(QtCore.QRect(160, 0, 161, 31))
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_your_cab.setFont(font)

        # Кнопка Админ
        self.button_admin = QtWidgets.QPushButton(dialog)
        self.button_admin.setGeometry(QtCore.QRect(320, 0, 161, 31))
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_admin.setFont(font)

        self.button_buy_item = QtWidgets.QPushButton(dialog)
        self.button_buy_item.setGeometry(QtCore.QRect(320, 350, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_buy_item.setFont(font)

        self.button_delete_item_delete = QtWidgets.QPushButton(dialog)
        self.button_delete_item_delete.setGeometry(QtCore.QRect(320, 320, 160, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.button_delete_item_delete.setFont(font)

        # ----------------Поля-----------------#

        self.spinBox_points = QtWidgets.QSpinBox(dialog)
        self.spinBox_points.setGeometry(QtCore.QRect(230, 200, 60, 30))
        self.spinBox_points.setMaximum(10000)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_points.setFont(font)

        # Поле со страницой
        self.spinBox_str = QtWidgets.QSpinBox(dialog)
        self.spinBox_str.setGeometry(QtCore.QRect(290, 431, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_str.setFont(font)
        self.spinBox_str.setMinimum(1)
        self.spinBox_str.setMaximum(2)

        # Поле с текстом Логин
        self.login = QtWidgets.QLineEdit(dialog)
        self.login.setGeometry(QtCore.QRect(310, 140, 180, 30))
        font.setFamily("Candara Light")
        font.setPointSize(16)
        self.login.setFont(font)

        # Поле с текстом Пароль
        self.password = QtWidgets.QLineEdit(dialog)
        self.password.setGeometry(QtCore.QRect(310, 180, 180, 30))
        font.setFamily("Candara Light")
        font.setPointSize(16)
        self.password.setFont(font)

        # Поле белый лист
        self.listView = QtWidgets.QListView(dialog)
        self.listView.setGeometry(QtCore.QRect(10, 130, 560, 290))
        self.listView.lower()

        # Поле Ввода "О нас"
        self.textEdit_about_us = QtWidgets.QTextEdit(dialog)
        self.textEdit_about_us.setEnabled(True)
        self.textEdit_about_us.setGeometry(QtCore.QRect(20, 200, 621, 271))

        self.comboBox = QtWidgets.QComboBox(dialog)
        self.comboBox.setGeometry(QtCore.QRect(310, 231, 111, 60))
        self.comboBox.addItems(["User", "Admin"])

        # ----------------Товары-----------------#

        # Товар
        self.item_1 = QtWidgets.QPushButton(dialog)
        self.item_1.setGeometry(QtCore.QRect(10, 130, 120, 120))
        font.setFamily("Candara")
        font.setPointSize(15)
        self.item_1.setFont(font)
        self.item_1.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Товар
        self.item_2 = QtWidgets.QPushButton(dialog)
        self.item_2.setGeometry(QtCore.QRect(150, 130, 120, 120))
        font.setFamily("Candara")
        font.setPointSize(15)
        self.item_2.setFont(font)
        self.item_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Товар
        self.item_3 = QtWidgets.QPushButton(dialog)
        self.item_3.setGeometry(QtCore.QRect(290, 130, 120, 120))
        font.setFamily("Candara")
        font.setPointSize(15)
        self.item_3.setFont(font)
        self.item_3.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Товар
        self.item_4 = QtWidgets.QPushButton(dialog)
        self.item_4.setGeometry(QtCore.QRect(430, 130, 120, 120))
        font.setFamily("Candara")
        font.setPointSize(15)
        self.item_4.setFont(font)
        self.item_4.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Товар
        self.item_5 = QtWidgets.QPushButton(dialog)
        self.item_5.setGeometry(QtCore.QRect(10, 270, 120, 120))
        font.setFamily("Candara")
        font.setPointSize(15)
        self.item_5.setFont(font)
        self.item_5.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Товар
        self.item_6 = QtWidgets.QPushButton(dialog)
        self.item_6.setGeometry(QtCore.QRect(150, 270, 120, 120))
        font.setFamily("Candara")
        font.setPointSize(15)
        self.item_6.setFont(font)
        self.item_6.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Товар
        self.item_7 = QtWidgets.QPushButton(dialog)
        self.item_7.setGeometry(QtCore.QRect(290, 270, 120, 120))
        font.setFamily("Candara")
        font.setPointSize(15)
        self.item_7.setFont(font)
        self.item_7.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Товар
        self.item_8 = QtWidgets.QPushButton(dialog)
        self.item_8.setGeometry(QtCore.QRect(430, 270, 120, 120))
        font.setFamily("Candara")
        font.setPointSize(15)
        self.item_8.setFont(font)
        self.item_8.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # ----------------Отдельно-----------------#

        # Установка текста
        self.button_entrance.setText("Войти")
        self.text_vhod.setText("Вход")
        self.button_back.setText("Назад")
        self.text_password.setText("Пароль:")
        self.text_error_log.setText("Вы ввели не правильные логин или пароль")
        self.button_main.setText("Главная")
        self.button_your_cab.setText("Личный кабинет")
        self.button_admin.setText("Admin")
        self.text_points.setText("100")
        self.text_things.setText("Товары")
        self.text_your_points.setText("Твои points:")
        self.button_your_cab.setText("Личный кабинет")
        self.text_points.setText("100")
        self.text_about_us.setText("Информация о пользоваетеле")
        self.text_login.setText("Логин:")
        self.text_role.setText("Роль:")
        self.text_login_login.setText("login")
        self.text_role_admin.setText("Admin")
        self.button_change_str.setText("Изменить")
        self.text_stranica.setText("Страница:")
        self.text_takoi_str_net.setText("Такой страницы нет!")
        self.button_shoping.setText("Покупки")
        self.button_history_add_points.setText("Начисления баллов")
        self.button_spisania.setText("Списания")
        self.button_history_user.setText("История пользователя")
        self.button_pokupki_user.setText("Покупки")
        self.button_nachis_user.setText("Начисления баллов")
        self.button_spisania_user.setText("Списания")
        self.text_enter_login.setText("Введите логин пользователя")
        self.button_points_change.setText("Баллы")
        self.button_things_change.setText("Товары")
        self.button_users_change.setText("Пользователи")
        self.text_admin.setText("Админ")
        self.button_about_us_change.setText("Изменить текст")
        self.button_add_item.setText("Добавить товар")
        self.button_delete_item.setText("Убрать товар")
        self.text_items.setText("Товары")
        self.button_add_points.setText("Начислить баллы")
        self.button_delete_points.setText("Снять баллы")
        self.button_admin_add_user.setText("Добавить пользователя")
        self.button_admin_access.setText("Изменить доступ")
        self.text_admin_users.setText("Пользователи")
        self.button_add_user_add.setText("Добавить")
        self.button_add_item_func.setText("Добавить товар")
        self.button_buy_item.setText("Купить товар")

        self.item_1.setText("Пусто")
        self.item_2.setText("Пусто")
        self.item_3.setText("Пусто")
        self.item_4.setText("Пусто")
        self.item_5.setText("Пусто")
        self.item_6.setText("Пусто")
        self.item_7.setText("Пусто")
        self.item_8.setText("Пусто")

        self.back_slide = "Начало"
        self.check_role = 0
        self.login_in = ""
        self.role_in = ""
        self.login_admin = ""

        # Функции вывода товаров в витрине
        
    def item_clicked_1(self):
        if self.item_1.text() == "Пусто":
            return
        if self.item_1.text() != "Пусто":
            self.closed()
            self.button_back.show()

            con = sqlite3.connect('auto/users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM Items WHERE name="{self.item_1.text()}";')
            value = cur.fetchall()

            info = value[0][2]
            price = value[0][3]

            self.text_things.setText(self.item_1.text())
            self.text_login_login.setText(f'{price}')
            self.text_login_login.setGeometry(QtCore.QRect(300, 160, 121, 31))
            self.text_things.setGeometry(QtCore.QRect(300, 130, 121, 31))
            self.textEdit_about_us.setEnabled(False)
            self.textEdit_about_us.setGeometry(QtCore.QRect(275, 200, 250, 120))
            self.textEdit_about_us.setText(info)

            self.text_role.setGeometry(QtCore.QRect(145, 130, 150, 31))
            self.text_login.setGeometry(QtCore.QRect(125, 160, 150, 31))
            self.text_about_us.setGeometry(QtCore.QRect(146, 190, 150, 31))
            self.text_role.setText("Название")
            self.text_login.setText("Цена")
            self.text_about_us.setText("Описание")

            self.text_login_login.show()
            self.text_things.show()
            self.textEdit_about_us.show()
            self.button_buy_item.show()
            self.text_role.show()
            self.text_login.show()
            self.text_about_us.show()

            self.back_slide = "item_clicked"

            if self.check_role == 1:
                self.entrance_admin_button()
            if self.check_role == 0:
                self.entrance_user_button()

    def item_clicked_2(self):
        if self.item_2.text() == "Пусто":
            return
        if self.item_2.text() != "Пусто":
            self.closed()
            self.button_back.show()

            con = sqlite3.connect('auto/users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM Items WHERE name="{self.item_2.text()}";')
            value = cur.fetchall()

            info = value[0][2]
            price = value[0][3]

            self.text_things.setText(self.item_2.text())
            self.text_login_login.setText(f'{price}')
            self.text_login_login.setGeometry(QtCore.QRect(300, 160, 121, 31))
            self.text_things.setGeometry(QtCore.QRect(300, 130, 121, 31))
            self.textEdit_about_us.setEnabled(False)
            self.textEdit_about_us.setGeometry(QtCore.QRect(275, 200, 250, 120))
            self.textEdit_about_us.setText(info)

            self.text_role.setGeometry(QtCore.QRect(145, 130, 150, 31))
            self.text_login.setGeometry(QtCore.QRect(125, 160, 150, 31))
            self.text_about_us.setGeometry(QtCore.QRect(146, 190, 150, 31))
            self.text_role.setText("Название")
            self.text_login.setText("Цена")
            self.text_about_us.setText("Описание")

            self.text_login_login.show()
            self.text_things.show()
            self.textEdit_about_us.show()
            self.button_buy_item.show()
            self.text_role.show()
            self.text_login.show()
            self.text_about_us.show()

            self.back_slide = "item_clicked"

            if self.check_role == 1:
                self.entrance_admin_button()
            if self.check_role == 0:
                self.entrance_user_button()

    def item_clicked_3(self):
        if self.item_3.text() == "Пусто":
            return
        if self.item_3.text() != "Пусто":
            self.closed()
            self.button_back.show()

            con = sqlite3.connect('auto/users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM Items WHERE name="{self.item_3.text()}";')
            value = cur.fetchall()

            info = value[0][2]
            price = value[0][3]

            self.text_things.setText(self.item_3.text())
            self.text_login_login.setText(f'{price}')
            self.text_login_login.setGeometry(QtCore.QRect(300, 160, 121, 31))
            self.text_things.setGeometry(QtCore.QRect(300, 130, 121, 31))
            self.textEdit_about_us.setEnabled(False)
            self.textEdit_about_us.setGeometry(QtCore.QRect(275, 200, 250, 120))
            self.textEdit_about_us.setText(info)

            self.text_role.setGeometry(QtCore.QRect(145, 130, 150, 31))
            self.text_login.setGeometry(QtCore.QRect(125, 160, 150, 31))
            self.text_about_us.setGeometry(QtCore.QRect(146, 190, 150, 31))
            self.text_role.setText("Название")
            self.text_login.setText("Цена")
            self.text_about_us.setText("Описание")

            self.text_login_login.show()
            self.text_things.show()
            self.textEdit_about_us.show()
            self.button_buy_item.show()
            self.text_role.show()
            self.text_login.show()
            self.text_about_us.show()

            self.back_slide = "item_clicked"

            if self.check_role == 1:
                self.entrance_admin_button()
            if self.check_role == 0:
                self.entrance_user_button()

    def item_clicked_4(self):
        if self.item_4.text() == "Пусто":
            return
        if self.item_4.text() != "Пусто":
            self.closed()
            self.button_back.show()

            con = sqlite3.connect('auto/users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM Items WHERE name="{self.item_4.text()}";')
            value = cur.fetchall()

            info = value[0][2]
            price = value[0][3]

            self.text_things.setText(self.item_4.text())
            self.text_login_login.setText(f'{price}')
            self.text_login_login.setGeometry(QtCore.QRect(300, 160, 121, 31))
            self.text_things.setGeometry(QtCore.QRect(300, 130, 121, 31))
            self.textEdit_about_us.setEnabled(False)
            self.textEdit_about_us.setGeometry(QtCore.QRect(275, 200, 250, 120))
            self.textEdit_about_us.setText(info)

            self.text_role.setGeometry(QtCore.QRect(145, 130, 150, 31))
            self.text_login.setGeometry(QtCore.QRect(125, 160, 150, 31))
            self.text_about_us.setGeometry(QtCore.QRect(146, 190, 150, 31))
            self.text_role.setText("Название")
            self.text_login.setText("Цена")
            self.text_about_us.setText("Описание")

            self.text_login_login.show()
            self.text_things.show()
            self.textEdit_about_us.show()
            self.button_buy_item.show()
            self.text_role.show()
            self.text_login.show()
            self.text_about_us.show()

            self.back_slide = "item_clicked"

            if self.check_role == 1:
                self.entrance_admin_button()
            if self.check_role == 0:
                self.entrance_user_button()

    def item_clicked_5(self):
        if self.item_5.text() == "Пусто":
            return
        if self.item_5.text() != "Пусто":
            self.closed()
            self.button_back.show()

            con = sqlite3.connect('auto/users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM Items WHERE name="{self.item_5.text()}";')
            value = cur.fetchall()

            info = value[0][2]
            price = value[0][3]

            self.text_things.setText(self.item_5.text())
            self.text_login_login.setText(f'{price}')
            self.text_login_login.setGeometry(QtCore.QRect(300, 160, 121, 31))
            self.text_things.setGeometry(QtCore.QRect(300, 130, 121, 31))
            self.textEdit_about_us.setEnabled(False)
            self.textEdit_about_us.setGeometry(QtCore.QRect(275, 200, 250, 120))
            self.textEdit_about_us.setText(info)

            self.text_role.setGeometry(QtCore.QRect(145, 130, 150, 31))
            self.text_login.setGeometry(QtCore.QRect(125, 160, 150, 31))
            self.text_about_us.setGeometry(QtCore.QRect(146, 190, 150, 31))
            self.text_role.setText("Название")
            self.text_login.setText("Цена")
            self.text_about_us.setText("Описание")

            self.text_login_login.show()
            self.text_things.show()
            self.textEdit_about_us.show()
            self.button_buy_item.show()
            self.text_role.show()
            self.text_login.show()
            self.text_about_us.show()

            self.back_slide = "item_clicked"

            if self.check_role == 1:
                self.entrance_admin_button()
            if self.check_role == 0:
                self.entrance_user_button()

    def item_clicked_6(self):
        if self.item_6.text() == "Пусто":
            return
        if self.item_6.text() != "Пусто":
            self.closed()
            self.button_back.show()

            con = sqlite3.connect('auto/users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM Items WHERE name="{self.item_6.text()}";')
            value = cur.fetchall()

            info = value[0][2]
            price = value[0][3]

            self.text_things.setText(self.item_6.text())
            self.text_login_login.setText(f'{price}')
            self.text_login_login.setGeometry(QtCore.QRect(300, 160, 121, 31))
            self.text_things.setGeometry(QtCore.QRect(300, 130, 121, 31))
            self.textEdit_about_us.setEnabled(False)
            self.textEdit_about_us.setGeometry(QtCore.QRect(275, 200, 250, 120))
            self.textEdit_about_us.setText(info)

            self.text_role.setGeometry(QtCore.QRect(145, 130, 150, 31))
            self.text_login.setGeometry(QtCore.QRect(125, 160, 150, 31))
            self.text_about_us.setGeometry(QtCore.QRect(146, 190, 150, 31))
            self.text_role.setText("Название")
            self.text_login.setText("Цена")
            self.text_about_us.setText("Описание")

            self.text_login_login.show()
            self.text_things.show()
            self.textEdit_about_us.show()
            self.button_buy_item.show()
            self.text_role.show()
            self.text_login.show()
            self.text_about_us.show()

            self.back_slide = "item_clicked"

            if self.check_role == 1:
                self.entrance_admin_button()
            if self.check_role == 0:
                self.entrance_user_button()

    def item_clicked_7(self):
        if self.item_7.text() == "Пусто":
            return
        if self.item_7.text() != "Пусто":
            self.closed()
            self.button_back.show()

            con = sqlite3.connect('auto/users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM Items WHERE name="{self.item_7.text()}";')
            value = cur.fetchall()

            info = value[0][2]
            price = value[0][3]

            self.text_things.setText(self.item_7.text())
            self.text_login_login.setText(f'{price}')
            self.text_login_login.setGeometry(QtCore.QRect(300, 160, 121, 31))
            self.text_things.setGeometry(QtCore.QRect(300, 130, 121, 31))
            self.textEdit_about_us.setEnabled(False)
            self.textEdit_about_us.setGeometry(QtCore.QRect(275, 200, 250, 120))
            self.textEdit_about_us.setText(str(info))

            self.text_role.setGeometry(QtCore.QRect(145, 130, 150, 31))
            self.text_login.setGeometry(QtCore.QRect(125, 160, 150, 31))
            self.text_about_us.setGeometry(QtCore.QRect(146, 190, 150, 31))
            self.text_role.setText("Название")
            self.text_login.setText("Цена")
            self.text_about_us.setText("Описание")

            self.text_login_login.show()
            self.text_things.show()
            self.textEdit_about_us.show()
            self.button_buy_item.show()
            self.text_role.show()
            self.text_login.show()
            self.text_about_us.show()

            self.back_slide = "item_clicked"

            if self.check_role == 1:
                self.entrance_admin_button()
            if self.check_role == 0:
                self.entrance_user_button()

    def item_clicked_8(self):
        if self.item_8.text() == "Пусто":
            return
        if self.item_8.text() != "Пусто":
            self.closed()
            self.button_back.show()

            con = sqlite3.connect('auto/users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM Items WHERE name="{self.item_8.text()}";')
            value = cur.fetchall()

            info = value[0][2]
            price = value[0][3]

            self.text_things.setText(self.item_8.text())
            self.text_login_login.setText(f'{price}')
            self.text_login_login.setGeometry(QtCore.QRect(300, 160, 121, 31))
            self.text_things.setGeometry(QtCore.QRect(300, 130, 121, 31))
            self.textEdit_about_us.setEnabled(False)
            self.textEdit_about_us.setGeometry(QtCore.QRect(275, 200, 250, 120))
            self.textEdit_about_us.setText(info)

            self.text_role.setGeometry(QtCore.QRect(145, 130, 150, 31))
            self.text_login.setGeometry(QtCore.QRect(125, 160, 150, 31))
            self.text_about_us.setGeometry(QtCore.QRect(146, 190, 150, 31))
            self.text_role.setText("Название")
            self.text_login.setText("Цена")
            self.text_about_us.setText("Описание")

            self.text_login_login.show()
            self.text_things.show()
            self.textEdit_about_us.show()
            self.button_buy_item.show()
            self.text_role.show()
            self.text_login.show()
            self.text_about_us.show()

            self.back_slide = "item_clicked"

            if self.check_role == 1:
                self.entrance_admin_button()
            if self.check_role == 0:
                self.entrance_user_button()

         # Удаление товара
    def delete_item(self):
        con = sqlite3.connect('auto/users.db')
        cur = con.cursor()

        name = self.login.text()

        if name == "":
            self.text_error_log.setText("Вы не ввели данные")
            self.text_error_log.setGeometry(QtCore.QRect(205, 360, 385, 30))
            self.text_error_log.show()
            timer = Timer(3.00, self.text_error_log.close)
            timer.start()

        if name != "":
            cur.execute(f'SELECT * FROM Items WHERE name="{name}";')
            value = cur.fetchall()

            if not value:
                self.text_error_log.setText(f'Нет товара с именем {name}')
                self.text_error_log.setGeometry(QtCore.QRect(205, 360, 385, 30))
                self.text_error_log.show()
                timer = Timer(3.00, self.text_error_log.close)
                timer.start()

            if value:
                cur.execute(f'DELETE FROM Items WHERE name="{name}";')
                con.commit()

                cur.close()
                con.close()

                self.text_error_log.setText(f'Вы удалили товар {name}')
                self.text_error_log.setGeometry(QtCore.QRect(205, 360, 385, 30))
                self.text_error_log.show()
                timer = Timer(3.00, self.text_error_log.close)
                timer.start()

                self.item_1.setText("Пусто")
                self.item_2.setText("Пусто")
                self.item_3.setText("Пусто")
                self.item_4.setText("Пусто")
                self.item_5.setText("Пусто")
                self.item_6.setText("Пусто")
                self.item_7.setText("Пусто")
                self.item_8.setText("Пусто")

                self.items_clicked()

    def button_delete_item_clicked(self):
        self.closed()
        self.button_back.show()

        self.text_login.setText("Название:")
        self.text_login.setGeometry(QtCore.QRect(170, 140, 180, 30))
        self.login.setGeometry(QtCore.QRect(310, 140, 180, 30))
        self.login.show()
        self.text_login.show()
        self.button_delete_item_delete.setText("Удалить")
        self.button_delete_item_delete.show()

        if self.check_role == 1:
            self.entrance_admin_button()
        if self.check_role == 0:
            self.entrance_user_button()
        self.back_slide = "button_delete_item_clicked"
    
    # Покупка товара
    def buy_item(self):
        name = self.text_things.text()
        price = self.text_login_login.text()
        user_log = self.login_admin

        con = sqlite3.connect('auto/users.db')
        cur = con.cursor()

        cur.execute(f'SELECT * FROM users WHERE login="{user_log}";')
        value = cur.fetchall()

        points = value[0][3]

        if points < int(price):
            self.text_error_log.setText("У вас не достаточно средств")
            self.text_error_log.setGeometry(QtCore.QRect(205, 390, 385, 30))
            self.text_error_log.show()
            timer = Timer(3.00, self.text_error_log.close)
            timer.start()
        if points > int(price):
            points = points - int(price)
            cur.execute(f'UPDATE users SET Points ="{points}" WHERE login="{user_log}";')

            now = datetime.now()
            current_time = now.strftime('Дата %D Время %H/%M/%S')

            cur.execute(f'INSERT INTO ItemsTransaction (UserLog, ItemName, Price, Time)'
                        f'VALUES ("{user_log}", "{name}", "{price}", "{current_time}");')
            con.commit()

            self.text_error_log.setText(f'Вы купили {name} за {price}')
            self.text_error_log.setGeometry(QtCore.QRect(205, 390, 385, 30))
            self.text_error_log.show()
            timer = Timer(3.00, self.text_error_log.close)
            timer.start()

        cur.close()
        con.close()

    def button_add_item_func_clicked(self):
        name = self.login.text()
        price = self.spinBox_points.value()
        info = self.textEdit_about_us.toPlainText()

        if name == "" or price == 0 or info == "":
            self.text_error_log.setText("Вы не ввели все данные")
            self.text_error_log.setGeometry(QtCore.QRect(205, 360, 385, 30))
            self.text_error_log.show()
            timer = Timer(3.00, self.text_error_log.close)
            timer.start()

        if name != "" and price != 0 and info != "":
            con = sqlite3.connect('auto/users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM Items WHERE name="{name}";')
            value = cur.fetchall()

            if value:
                self.text_error_log.setText("Товар с таким именем уже есть")
                self.text_error_log.setGeometry(QtCore.QRect(205, 360, 385, 30))
                self.text_error_log.show()
                timer = Timer(3.00, self.text_error_log.close)
                timer.start()
            if not value:
                con = sqlite3.connect('auto/users.db')
                cur = con.cursor()

                cur.execute(f'INSERT INTO Items (name, info, price)'
                            f'VALUES ("{name}", "{info}", {price});')

                con.commit()

                self.text_error_log.setGeometry(QtCore.QRect(205, 360, 385, 30))
                self.text_error_log.setText(f'Был создан товар {name}')
                self.text_error_log.show()

                timer = Timer(3.00, self.text_error_log.close)
                timer.start()

                self.admin_menu()

                cur.close()
                con.close()

                if self.item_1.text() == "Пусто":
                    self.item_1.setText(f'{name}')
                elif self.item_2.text() == "Пусто":
                    self.item_2.setText(f'{name}')
                elif self.item_3.text() == "Пусто":
                    self.item_3.setText(f'{name}')
                elif self.item_4.text() == "Пусто":
                    self.item_4.setText(f'{name}')
                elif self.item_5.text() == "Пусто":
                    self.item_5.setText(f'{name}')
                elif self.item_6.text() == "Пусто":
                    self.item_6.setText(f'{name}')
                elif self.item_7.text() == "Пусто":
                    self.item_7.setText(f'{name}')
                elif self.item_8.text() == "Пусто":
                    self.item_8.setText(f'{name}')
                else:
                    return
    # Функция смены роли у пользователя
    def admin_users_change_role_clicked(self):
        con = sqlite3.connect('auto/users.db')
        cur = con.cursor()

        login = self.login.text()
        role = self.comboBox.currentText()
        rolee = 1

        cur.execute(f'SELECT * FROM users WHERE login="{login}";')
        value = cur.fetchall()
        cur.close()
        con.close()

        if login == "":
            self.text_error_log.setText("Вы не ввели данные")
            self.text_error_log.setGeometry(QtCore.QRect(205, 360, 385, 30))
            self.text_error_log.show()
            timer = Timer(3.00, self.text_error_log.close)
            timer.start()

        if login != "":
            if not value:
                self.text_error_log.setText("Вы ввели не существующий логин")
                self.text_error_log.setGeometry(QtCore.QRect(205, 360, 385, 30))
                self.text_error_log.show()
                timer = Timer(3.00, self.text_error_log.close)
                timer.start()

            if value:

                if role == "Открыть":
                    rolee = 1
                if role == "Закрыть":
                    rolee = 0

                con = sqlite3.connect('auto/users.db')
                cur = con.cursor()
                cur.execute(f'UPDATE users SET Access ={rolee} WHERE login="{login}";')

                con.commit()

                self.text_error_log.setGeometry(QtCore.QRect(205, 360, 385, 30))
                self.text_error_log.setText(f'у {login}, доступ был изменен на "{role}"')
                self.text_error_log.show()

                timer = Timer(3.00, self.text_error_log.close)
                timer.start()

                self.admin_menu()

                cur.close()
                con.close()
   # Функция смены доступа у пользователя
    def admin_users_change_clicked(self):
        self.closed()
        self.button_back.show()

        self.text_admin_users.setText("Изменить доступ")
        self.text_login_login.setText("Логин:")
        self.button_change_role.setText("Изменить")
        self.text_admin_users.setGeometry(QtCore.QRect(290, 50, 220, 31))
        self.text_login_login.setGeometry(QtCore.QRect(200, 140, 120, 30))
        self.text_role.setGeometry(QtCore.QRect(200, 180, 120, 30))
        self.comboBox.setGeometry(QtCore.QRect(310, 180, 120, 30))
        self.comboBox.clear()
        self.comboBox.addItems(["Открыть", "Закрыть"])

        self.button_change_role.show()
        self.text_admin_users.show()
        self.login.show()
        self.text_login_login.show()
        self.text_role.show()
        self.comboBox.show()

        if self.check_role == 1:
            self.entrance_admin_button()
        if self.check_role == 0:
            self.entrance_user_button()

        self.back_slide = "admin_users_change_clicked"

           # Добавление пользователя
    def admin_users_add_clicked_button(self):
        con = sqlite3.connect('auto/users.db')
        cur = con.cursor()

        login = self.login.text()
        passw = self.password.text()
        role = self.comboBox.currentText()

        if role == "User":
            role = 0
        if role == "Admin":
            role = 1

        cur.execute(f'SELECT * FROM users WHERE login="{login}";')
        value = cur.fetchall()
        cur.close()
        con.close()

        if login == "" or passw == "":
            self.text_error_log.setText("Вы не ввели данные")
            self.text_error_log.setGeometry(QtCore.QRect(205, 360, 385, 30))
            self.text_error_log.show()
            timer = Timer(3.00, self.text_error_log.close)
            timer.start()

        if value:
            self.text_error_log.setText("Вы ввели существующий логин")
            self.text_error_log.setGeometry(QtCore.QRect(205, 360, 385, 30))
            self.text_error_log.show()
            timer = Timer(3.00, self.text_error_log.close)
            timer.start()

        if login != "" and passw != "":
            if not value:
                con = sqlite3.connect('auto/users.db')
                cur = con.cursor()
                cur.execute(f'INSERT INTO users (login, password, Role, Access)'
                            f'VALUES ("{login}", "{passw}", {role}, {1});')

                con.commit()

                if role == 0:
                    role = "User"
                if role == 1:
                    role = "Admin"

                self.text_error_log.setGeometry(QtCore.QRect(205, 360, 385, 30))
                self.text_error_log.setText(f'{login}, был добавилен как {role}')
                self.text_error_log.show()

                timer = Timer(3.00, self.text_error_log.close)
                timer.start()

                self.admin_menu()

                cur.close()
                con.close()

    def admin_users_add_clicked(self):
        self.closed()
        self.button_back.show()

        self.comboBox.addItems(["User", "Admin"])
        self.text_admin_users.setText("Добавить пользователя")
        self.text_login_login.setText("Логин:")
        self.text_admin_users.setGeometry(QtCore.QRect(290, 50, 220, 31))
        self.text_login_login.setGeometry(QtCore.QRect(200, 140, 120, 30))
        self.text_role.setGeometry(QtCore.QRect(200, 220, 120, 30))
        self.comboBox.setGeometry(QtCore.QRect(310, 220, 120, 30))

        self.text_admin_users.show()
        self.login.show()
        self.password.show()
        self.text_password.show()
        self.text_login_login.show()
        self.text_role.show()
        self.comboBox.show()
        self.button_add_user_add.show()

        if self.check_role == 1:
            self.entrance_admin_button()
        if self.check_role == 0:
            self.entrance_user_button()

        self.back_slide = "admin_users_add_clicked"

    def admin_users_clicked(self):
        self.closed()
        self.button_back.show()
        self.button_admin_add_user.show()
        self.button_admin_access.show()
        self.text_admin_users.setGeometry(QtCore.QRect(330, 50, 121, 31))
        self.text_admin_users.setText("Пользователи")
        self.text_admin_users.show()

        if self.check_role == 1:
            self.entrance_admin_button()
        if self.check_role == 0:
            self.entrance_user_button()

        self.back_slide = "admin_users_clicked"

    # Добавление баллов
    def add_points_clicked(self):
        login = self.login.text()
        kol = self.spinBox_points.value()
        inf = self.textEdit_about_us.toPlainText()

        if login == "" or inf == "" or kol == 0:

            self.text_error_log.setGeometry(QtCore.QRect(200, 380, 400, 31))
            self.text_error_log.setText("Вы не заполнили все данные")
            self.text_error_log.show()

            timer = Timer(3.00, self.text_error_log.close)
            timer.start()

        if login != "" and inf != "" and kol != 0:
            con = sqlite3.connect('auto/users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM users WHERE login="{login}";')
            value = cur.fetchall()

            if not value:
                self.text_error_log.setGeometry(QtCore.QRect(200, 380, 400, 31))
                self.text_error_log.setText("Вы ввели не существующий логин")
                self.text_error_log.show()

                timer = Timer(3.00, self.text_error_log.close)
                timer.start()

            if value:
                cur.execute(f'SELECT * FROM users WHERE login="{login}";')
                value = cur.fetchall()
                summa = value[0][3]
                summa = summa + kol
                cur.execute(f'UPDATE users SET Points ="{summa}" WHERE login="{login}";')
                con.commit()

                now = datetime.now()
                current_time = now.strftime('Дата %D Время %H/%M/%S')

                cur.execute(f'INSERT INTO PointsTransaction (AdminLog, ChangePTS, TransactionTime, Info, UserLogin, '
                            f'Type) '
                            f'VALUES ("{str(self.login_admin)}", {int(kol)}, "{current_time}", "{str(inf)}", '
                            f'"{str(login)}", "Начисление");')

                con.commit()

                self.text_error_log.setGeometry(QtCore.QRect(150, 350, 450, 31))
                self.text_error_log.setText(f'{kol} баллов были успешно начислены {login}')
                self.text_error_log.show()

                timer = Timer(3.00, self.text_error_log.close)
                timer.start()

                self.admin_menu()

    # снятие баллов
    def delete_points_clicked(self):
        login = self.login.text()
        kol = self.spinBox_points.value()
        inf = self.textEdit_about_us.toPlainText()

        if login == "" or inf == "" or kol == 0:

            self.text_error_log.setGeometry(QtCore.QRect(200, 380, 400, 31))
            self.text_error_log.setText("Вы не заполнили все данные")
            self.text_error_log.show()

            timer = Timer(3.00, self.text_error_log.close)
            timer.start()

        if login != "" and inf != "" and kol != 0:
            con = sqlite3.connect('auto/users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM users WHERE login="{login}";')
            value = cur.fetchall()

            if not value:
                self.text_error_log.setGeometry(QtCore.QRect(200, 380, 400, 31))
                self.text_error_log.setText("Вы ввели не существующий логин")
                self.text_error_log.show()

                timer = Timer(3.00, self.text_error_log.close)
                timer.start()

            if value:
                cur.execute(f'SELECT * FROM users WHERE login="{login}";')
                value = cur.fetchall()
                summa = value[0][3]

                if int(summa) < kol:
                    self.text_error_log.show()
                    self.text_error_log.setText("Вы ввели недопустимое значение")
                    timer = Timer(3.00, self.text_error_log.close)
                    timer.start()

                if int(summa) > kol:
                    summa = summa - kol
                    cur.execute(f'UPDATE users SET Points ="{summa}" WHERE login="{login}";')

                    now = datetime.now()
                    current_time = now.strftime("Дата %D Время %H/%M/%S")

                    cur.execute(f'INSERT INTO PointsTransaction (AdminLog, ChangePTS, TransactionTime, Info, '
                                f'UserLogin, Type) '
                                f'VALUES ("{self.login_admin}", {kol}, "{current_time}", "{inf}", "{login}", '
                                f'"Списание");')
                    con.commit()

                    self.text_error_log.setGeometry(QtCore.QRect(150, 350, 450, 31))
                    self.text_error_log.setText(f'{kol} баллов были успешно списаны {login}')
                    self.text_error_log.show()

                    timer = Timer(3.00, self.text_error_log.close)
                    timer.start()

                    self.admin_menu()

    def points_clicked(self):
        self.closed()
        self.clear()

        self.text_login.setText("Логин пользователя")
        self.text_login_login.setText("Количество баллов")
        self.text_vhod.setText("Информация")
        self.text_login.setGeometry(QtCore.QRect(1, 150, 200, 31))
        self.text_login_login.setGeometry(QtCore.QRect(1, 200, 200, 31))
        self.login.setGeometry(QtCore.QRect(230, 150, 150, 30))
        self.textEdit_about_us.setGeometry(QtCore.QRect(400, 150, 300, 100))
        self.text_vhod.setGeometry(QtCore.QRect(485, 125, 130, 20))

        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        self.text_vhod.setFont(font)

        self.text_login.show()
        self.text_login_login.show()
        self.login.show()
        self.textEdit_about_us.show()

        self.button_back.show()
        self.button_add_points.show()
        self.button_delete_points.show()
        self.spinBox_points.show()
        self.text_vhod.show()

        if self.check_role == 1:
            self.entrance_admin_button()
        if self.check_role == 0:
            self.entrance_user_button()
        self.back_slide = "points_clicked"

    def button_add_item_clicked(self):
        self.closed()
        self.button_back.show()
        self.text_items.setGeometry(QtCore.QRect(320, 50, 144, 31))
        self.text_items.setText("Добавить товар")
        self.text_login_login.setGeometry(QtCore.QRect(210, 180, 150, 31))
        self.text_login.setGeometry(QtCore.QRect(210, 220, 150, 31))
        self.text_about_us.setGeometry(QtCore.QRect(210, 260, 150, 31))
        self.spinBox_points.setGeometry(QtCore.QRect(340, 220, 150, 31))
        self.login.setGeometry(QtCore.QRect(340, 180, 150, 31))
        self.textEdit_about_us.setGeometry(QtCore.QRect(340, 260, 200, 50))

        self.text_login_login.setText("Название")
        self.text_login.setText("Цена")
        self.text_about_us.setText("Описание")

        self.text_items.show()
        self.button_add_item_func.show()

        self.text_login_login.show()
        self.text_login.show()
        self.text_about_us.show()
        self.spinBox_points.show()
        self.login.show()
        self.textEdit_about_us.show()

        if self.check_role == 1:
            self.entrance_admin_button()
        if self.check_role == 0:
            self.entrance_user_button()
        self.back_slide = "button_add_item_clicked"

    def items_clicked(self):
        self.closed()
        self.button_back.show()
        self.button_add_item.show()
        self.button_delete_item.show()
        self.text_items.setGeometry(QtCore.QRect(330, 50, 121, 31))

        self.text_items.setText("Товары")
        self.text_items.show()

        if self.check_role == 1:
            self.entrance_admin_button()
        if self.check_role == 0:
            self.entrance_user_button()
        self.back_slide = "items_clicked"

    def clear(self):
        # Функция очистки полей
        self.login.clear()
        self.password.clear()
        self.spinBox_points.clear()
        self.textEdit_about_us.clear()

    def back(self):
        # Функция НАЗАД
        self.clear()
        if self.back_slide == "История пользователя":
            self.clicked_history()
        if self.back_slide == "items_clicked":
            self.admin_menu()
        if self.back_slide == "points_clicked":
            self.admin_menu()
        if self.back_slide == "admin_users_clicked":
            self.admin_menu()
        if self.back_slide == "admin_users_add_clicked":
            self.admin_users_clicked()
        if self.back_slide == "admin_users_change_clicked":
            self.admin_users_clicked()
        if self.back_slide == "button_add_item_clicked":
            self.items_clicked()
        if self.back_slide == "item_clicked":
            self.entrance_main_button()
        if self.back_slide == "button_delete_item_clicked":
            self.items_clicked()
    
    # Основаня функция закрытие окон и объектов
    def closed(self):
        # Закрытие всех элементов
        self.clear()
        self.button_about_us_change.close()
        self.button_entrance.close()
        self.button_back.close()
        self.text_vhod.close()
        self.password.close()
        self.login.close()
        self.text_password.close()
        self.text_login.close()

        self.text_your_points.close()
        self.button_main.close()
        self.button_your_cab.close()
        self.button_admin.close()
        self.text_points.close()
        self.listView.close()
        self.text_things.close()
        self.text_stranica.close()
        self.text_takoi_str_net.close()
        self.button_change_str.close()
        self.spinBox_str.close()
        self.button_add_user_add.close()

        self.text_your_points.close()
        self.text_about_us.close()
        self.text_role.close()
        self.text_login_login.close()
        self.text_role_admin.close()
        self.textEdit_about_us.close()

        self.button_shoping.close()
        self.button_history_add_points.close()
        self.button_spisania.close()
        self.button_history_user.close()

        self.button_pokupki_user.close()
        self.button_nachis_user.close()
        self.button_spisania_user.close()
        self.text_enter_login.close()
        self.login.close()

        self.button_points_change.close()
        self.button_things_change.close()
        self.button_users_change.close()
        self.text_admin.close()

        self.button_add_item.close()
        self.button_delete_item.close()
        self.text_items.close()

        self.button_add_points.close()
        self.button_delete_points.close()
        self.spinBox_points.close()

        self.button_admin_add_user.close()
        self.button_admin_access.close()
        self.text_admin_users.close()
        self.comboBox.close()
        self.button_change_role.close()
        self.button_add_item_func.close()

        self.button_buy_item.close()
        self.button_delete_item_delete.close()

        self.item_1.close()
        self.item_2.close()
        self.item_3.close()
        self.item_4.close()
        self.item_5.close()
        self.item_6.close()
        self.item_7.close()
        self.item_8.close()

        self.text_vhod.setText("Вход")
        self.text_login.setText("Логин:")
        self.text_things.setText("Товары")
        self.text_role.setText("Роль:")

        self.text_things.setGeometry(QtCore.QRect(260, 90, 111, 31))
        self.text_role.setGeometry(QtCore.QRect(170, 80, 71, 31))
        self.text_vhod.setGeometry(QtCore.QRect(250, 60, 300, 50))
        self.login.setGeometry(QtCore.QRect(310, 140, 180, 30))
        self.password.setGeometry(QtCore.QRect(310, 180, 180, 30))
        self.text_login_login.setGeometry(QtCore.QRect(240, 50, 71, 31))
        self.text_about_us.setGeometry(QtCore.QRect(180, 170, 281, 31))

        self.spinBox_points.setGeometry(QtCore.QRect(230, 200, 60, 30))

        self.text_login.setGeometry(QtCore.QRect(200, 140, 120, 30))
        self.text_items.setGeometry(QtCore.QRect(330, 50, 121, 31))

        self.textEdit_about_us.setGeometry(QtCore.QRect(20, 200, 621, 271))

        self.textEdit_about_us.setEnabled(True)

        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(35)
        self.text_vhod.setFont(font)

    def beginning(self):
        # Открытие начального экрана авторизации
        self.closed()
        self.closed()
        self.text_error_log.close()
        self.text_vhod.show()
        self.password.show()
        self.login.show()
        self.text_password.show()
        self.text_login.show()
        self.button_entrance.show()

    def person_cab(self):
        self.closed()
        self.textEdit_about_us.setGeometry(QtCore.QRect(20, 200, 621, 271))
        self.point_get()
        self.text_your_points.show()
        self.text_about_us.show()
        self.text_login.show()
        self.text_role.show()
        self.text_points.show()
        self.login_get()
        self.text_login_login.show()
        self.text_role_admin.show()
        self.textedit_about_us_def()
        self.textEdit_about_us.show()
        self.button_about_us_change.show()
        self.text_login.setGeometry(QtCore.QRect(170, 50, 71, 31))
        self.back_slide = "Личный кабинет"

        if self.check_role == 1:
            self.entrance_admin_button()
        if self.check_role == 0:
            self.entrance_user_button()
            self.text_role_admin.setText("User")

    def entrance_user_button(self):
        self.button_main.show()
        self.button_your_cab.show()

    def entrance_admin_button(self):
        self.button_main.show()
        self.button_your_cab.show()
        self.button_admin.show()

    def entrance_main_button(self):
        if self.check_role == 1:
            self.entrance_admin()
        if self.check_role == 0:
            self.entrance_user()
     #  Вывод витрины товаров на экран
    def entrance_item(self):
        con = sqlite3.connect('auto/users.db')
        cur = con.cursor()

        cur.execute(f'SELECT * FROM Items;')
        value = cur.fetchall()
        i = 0
        if len(value) > i:
            if value[0][1]:
                name_1 = value[0][1]
                self.item_1.setText(f'{name_1}')
                i = i + 1
        if len(value) > i:
            if value[1][1]:
                name_2 = value[1][1]
                self.item_2.setText(f'{name_2}')
                i = i + 1
        if len(value) > i:
            if value[2][1]:
                name_3 = value[2][1]
                self.item_3.setText(f'{name_3}')
                i = i + 1
        if len(value) > i:
            if value[3][1]:
                name_4 = value[3][1]
                self.item_4.setText(f'{name_4}')
                i = i + 1
        if len(value) > i:
            if value[4][1]:
                name_5 = value[4][1]
                self.item_5.setText(f'{name_5}')
                i = i + 1
        if len(value) > i:
            if value[5][1]:
                name_6 = value[5][1]
                self.item_6.setText(f'{name_6}')
                i = i + 1
        if len(value) > i:
            if value[6][1]:
                name_7 = value[6][1]
                self.item_7.setText(f'{name_7}')
                i = i + 1
        if len(value) > i:
            if value[7][1]:
                name_8 = value[7][1]
                self.item_8.setText(f'{name_8}')

        self.item_1.show()
        self.item_2.show()
        self.item_3.show()
        self.item_4.show()
        self.item_5.show()
        self.item_6.show()
        self.item_7.show()
        self.item_8.show()

    def entrance_user(self):
        self.closed()
        self.text_points.setGeometry(QtCore.QRect(10, 60, 111, 31))
        self.point_get()
        self.text_your_points.show()
        self.button_main.show()
        self.button_your_cab.show()
        self.text_points.show()
        self.listView.show()
        self.listView.setGeometry(QtCore.QRect(10, 130, 631, 290))
        self.text_things.show()

        self.entrance_item()

        self.back_slide = "Вход User"
        self.check_role = 0

    def entrance_admin(self):
        self.closed()
        self.text_points.setGeometry(QtCore.QRect(10, 60, 111, 31))
        self.point_get()
        self.text_your_points.show()
        self.button_main.show()
        self.button_your_cab.show()
        self.button_admin.show()
        self.text_points.show()
        self.listView.show()
        self.listView.setGeometry(QtCore.QRect(10, 130, 560, 290))

        self.text_things.show()

        self.entrance_item()

        self.back_slide = "Вход Admin"
        self.check_role = 1

    def clicked_history(self):
        self.closed()
        self.listView.show()
        self.listView.setGeometry(QtCore.QRect(10, 90, 581, 351))
        self.button_shoping.show()
        self.button_history_add_points.show()
        self.button_spisania.show()
        self.back_slide = "История"

        if self.check_role == 1:
            self.button_history_user.show()

        if self.check_role == 1:
            self.entrance_admin_button()
        if self.check_role == 0:
            self.entrance_user_button()

    def clicked_history_user(self):
        self.closed()
        self.clear()
        self.button_pokupki_user.show()
        self.button_nachis_user.show()
        self.button_spisania_user.show()
        self.text_enter_login.show()
        self.button_back.show()
        self.login.show()
        self.login.setGeometry(QtCore.QRect(210, 230, 151, 21))

        self.back_slide = "История пользователя"

        if self.check_role == 1:
            self.entrance_admin_button()
        if self.check_role == 0:
            self.entrance_user_button()

    def admin_menu(self):
        self.closed()
        self.entrance_admin_button()
        self.button_points_change.show()
        self.button_things_change.show()
        self.button_users_change.show()
        self.text_admin.show()

    def textedit_about_us_change(self):
        about_us = self.textEdit_about_us.toPlainText()
        login = self.login_in

        con = sqlite3.connect('auto/users.db')
        cur = con.cursor()
        cur.execute(f'UPDATE users SET About ="{about_us}" WHERE login="{login}";')

        con.commit()

    def textedit_about_us_def(self):
        con = sqlite3.connect('auto/users.db')
        cur = con.cursor()

        login = self.login_in

        cur.execute(f'SELECT * FROM users WHERE login="{login}";')
        value = cur.fetchall()

        about_us = value[0][5]

        self.textEdit_about_us.setText(str(about_us))
    # Получение логина для вывода
    def login_get(self):
        login = self.login_in
        role = self.role_in
        self.text_login_login.setText(str(login))
        self.text_role_admin.setText(str(role))
    # Получчение очков для вывода
    def point_get(self):
        con = sqlite3.connect('auto/users.db')
        cur = con.cursor()

        login = self.login_in

        cur.execute(f'SELECT * FROM users WHERE login="{login}";')
        value = cur.fetchall()

        point = value[0][3]

        self.text_points.setText(str(point))

    # Назначение роли в программе
    def entrance_check(self, login):
        con = sqlite3.connect('auto/users.db')
        cur = con.cursor()

        cur.execute(f'SELECT * FROM users WHERE login="{login}";')
        value = cur.fetchall()

        self.login_in = login

        if value[0][6] == 1:
            self.role_in = "Admin"

        if value[0][6] == 0:
            self.role_in = "User"

        if value != [] and value[0][6] == 1:
            self.entrance_admin()
        if value != [] and value[0][6] == 0:
            self.entrance_user()

    # Функция авторизации аккаунта, проверки его на доступ, правильность ввода данных
    def login_def(self, login, passw):
        con = sqlite3.connect('auto/users.db')
        cur = con.cursor()

        self.login_admin = login

        cur.execute(f'SELECT * FROM users WHERE login="{login}";')
        value = cur.fetchall()

        if value != [] and value[0][2] == passw:
            if value[0][7] == 0:
                self.text_error_log.setText("Этому аккаунту запрещен доступ")
                self.text_error_log.show()
            if value[0][7] == 1:
                self.entrance_check(login)
        if value != [] and value[0][2] != passw:
            self.text_error_log.setText("Вы ввели не правильные логин или пароль")
            self.text_error_log.show()
        if value == [] or value[0][2] != passw:
            self.text_error_log.setText("Вы ввели не правильные логин или пароль")
            self.text_error_log.show()

        cur.close()
        con.close()
