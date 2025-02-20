from PyQt5 import QtWidgets
from untitled import UiDialog
import sys


class Untitled(QtWidgets.QMainWindow):
    def __init__(self):
        # Присоединение окна
        super().__init__()
        self.ui = UiDialog(self)
        self.ui.setupui(self)

        self.ui.beginning()
        self.ui.button_back.clicked.connect(self.ui.back)
        self.ui.button_entrance.clicked.connect(self.wrapper)
        self.ui.button_your_cab.clicked.connect(self.ui.person_cab)
        self.ui.button_main.clicked.connect(self.ui.entrance_main_button)
        self.ui.button_history_user.clicked.connect(self.ui.clicked_history_user)
        self.ui.button_admin.clicked.connect(self.ui.admin_menu)
        self.ui.button_about_us_change.clicked.connect(self.ui.textedit_about_us_change)
        self.ui.button_things_change.clicked.connect(self.ui.items_clicked)
        self.ui.button_points_change.clicked.connect(self.ui.points_clicked)
        self.ui.button_add_points.clicked.connect(self.ui.add_points_clicked)
        self.ui.button_delete_points.clicked.connect(self.ui.delete_points_clicked)
        self.ui.button_users_change.clicked.connect(self.ui.admin_users_clicked)
        self.ui.button_admin_add_user.clicked.connect(self.ui.admin_users_add_clicked)
        self.ui.button_add_user_add.clicked.connect(self.ui.admin_users_add_clicked_button)
        self.ui.button_admin_access.clicked.connect(self.ui.admin_users_change_clicked)
        self.ui.button_change_role.clicked.connect(self.ui.admin_users_change_role_clicked)
        self.ui.button_add_item.clicked.connect(self.ui.button_add_item_clicked)
        self.ui.button_add_item_func.clicked.connect(self.ui.button_add_item_func_clicked)
        self.ui.button_buy_item.clicked.connect(self.ui.buy_item)
        self.ui.button_delete_item.clicked.connect(self.ui.button_delete_item_clicked)
        self.ui.button_delete_item_delete.clicked.connect(self.ui.delete_item)
        self.ui.item_1.clicked.connect(self.ui.item_clicked_1)
        self.ui.item_2.clicked.connect(self.ui.item_clicked_2)
        self.ui.item_3.clicked.connect(self.ui.item_clicked_3)
        self.ui.item_4.clicked.connect(self.ui.item_clicked_4)
        self.ui.item_5.clicked.connect(self.ui.item_clicked_5)
        self.ui.item_6.clicked.connect(self.ui.item_clicked_6)
        self.ui.item_7.clicked.connect(self.ui.item_clicked_7)
        self.ui.item_8.clicked.connect(self.ui.item_clicked_8)

    def wrapper(self):
        if len(self.ui.login.text()) == 0 and len(self.ui.password.text()) == 0:
            self.ui.text_error_log.show()
            self.ui.text_error_log.setText("Вы не ввели данные!")
        else:
            self.ui.text_error_log.close()
            self.auth()

    def auth(self):
        name = self.ui.login.text()
        passw = self.ui.password.text()
        self.ui.login_def(name, passw)


# Открытие главного окна
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Untitled()
    application.show()

    sys.exit(app.exec())
