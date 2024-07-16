# import QtGui module from PyQt5 package
from PyQt5 import QtGui, uic

# from QtWidgets found in package PyQt5 import classes QApplication - QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, \
    QRadioButton, QCheckBox, QTextEdit
import sys

from customers.company_handler import CompanyHandler
from orders.order import Order


class LoginScreen(QMainWindow):  # inheritance FirstWindow class inherit from QMainWindow class
    # static attributes
    current_order = Order()

    def __init__(self, master_module_reference):
        super().__init__()
        self.master_module_reference = master_module_reference

        # Load ui File
        uic.loadUi('login_module_ui.ui', self)

        # Define Widgets
        self.line_edit_username = self.findChild(QLineEdit, 'line_edit_username')
        self.line_edit_password = self.findChild(QLineEdit, 'line_edit_password')
        self.button_login = self.findChild(QPushButton, 'button_login')

        # Define Operation
        self.button_login.clicked.connect(self.func_check_login)

        # Show window
        self.show()

    def func_check_login(self): # static        username = ahmed        password = ahmed123
        # task : make dynamic check for user from a db table
        user_name = self.line_edit_username.text()
        password = self.line_edit_password.text()
        print(user_name, password)
        if user_name =='ahmed' and password == 'ahmed123':
            print('Valid login - Welcome')
            self.line_edit_username.setText('')
            self.line_edit_password.setText('')
            # set order
            LoginScreen.current_order.set_order_id(1001) # temp value
            LoginScreen.current_order.set_customer(CompanyHandler.get_company_by_id(2))
            print('test the current customer = ', LoginScreen.current_order.get_customer().get_customer_name())

            # hide login sub window , re-enable menu
            self.master_module_reference.mdi_area.closeAllSubWindows()
            self.master_module_reference.func_change_menu_visibility(True)
        else:
            print('Invalid user name or password - please try again')


# main program
# app_object = QApplication(sys.argv) # sys.argv : list of parameters used when open window from terminal [ not often ]
# widgets_window_object = LoginScreen()
# sys.exit(app_object.exec())  # exit screen only when user take action