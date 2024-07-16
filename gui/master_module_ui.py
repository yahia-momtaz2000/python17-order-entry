# import QtGui module from PyQt5 package
from PyQt5 import QtGui, uic

# from QtWidgets found in package PyQt5 import classes QApplication - QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, \
    QRadioButton, QCheckBox, QTextEdit, QMenu, QAction, QMdiArea
import sys

from gui import login_module_ui, software_module_ui


class MasterScreen(QMainWindow):  # inheritance FirstWindow class inherit from QMainWindow class
    def __init__(self):
        super().__init__()

        # Load ui File
        uic.loadUi('master_module_ui.ui', self)

        # Define Widgets
        # 1- define Menus
        self.menu_user_actions = self.findChild(QMenu, 'menu_user_actions')
        self.menu_products_setup = self.findChild(QMenu, 'menu_products_setup')

        # 2- Define Menu items
        self.action_logout = self.findChild(QAction, 'action_logout')
        self.action_exit_application = self.findChild(QAction, 'action_exit_application')
        self.action_software = self.findChild(QAction, 'action_software')
        self.action_hardware = self.findChild(QAction, 'action_hardware')
        self.action_manual = self.findChild(QAction, 'action_manual')

        # 3- Define Mdi Area widget
        self.mdi_area = self.findChild(QMdiArea, 'mdi_area')


        # Define Operations ??
        # self.action_logout.triggered.connect(self.func_logout)
        self.action_software.triggered.connect(self.func_open_software_screen)


        # Define initializers
        self.showMaximized()  # maximize the screen to full screen
        # maximize mdi area to full screen
        scr = QApplication.desktop()
        available_geometry = scr.availableGeometry()
        self.mdi_area.setGeometry(available_geometry)

        self.func_open_login_screen() # initially open the login screen

        # Show window
        self.show()

    def func_open_login_screen(self):
        self.login_screen = login_module_ui.LoginScreen(self)  # object from LoginScreen
        self.mdi_area.addSubWindow(self.login_screen)
        self.login_screen.show()

    def func_change_menu_visibility(self, is_valid):
        self.menu_user_actions.setEnabled(is_valid)
        self.menu_products_setup.setEnabled(is_valid)

    def func_open_software_screen(self):
        print('Open software screen function')
        self.software_screen = software_module_ui.SoftwareScreen(self)
        self.mdi_area.addSubWindow(self.software_screen)
        self.software_screen.show()


# main program
app_object = QApplication(sys.argv) # sys.argv : list of parameters used when open window from terminal [ not often ]
widgets_window_object = MasterScreen()
sys.exit(app_object.exec())  # exit screen only when user take action