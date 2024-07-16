# import QtGui module from PyQt5 package
import sys
from PyQt5 import QtGui, uic
# from QtWidgets found in package PyQt5 import classes QApplication - QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, \
    QRadioButton, QCheckBox, QTextEdit, QMenu, QAction, QMdiArea, QTableWidget, QTableWidgetItem

from customers.company_handler import CompanyHandler
from gui.login_module_ui import LoginScreen
from orders.order import Order
from orders.order_handler import OrderHandler
from orders.order_item import OrderItem
from products.software_handler import SoftwareHandler


class CartScreen(QMainWindow):  # inheritance FirstWindow class inherit from QMainWindow class
    def __init__(self):
        super().__init__()

        # Load ui File
        uic.loadUi('cart_module_ui.ui', self)

        # Link Widgets
        self.table_cart = self.findChild(QTableWidget, 'table_cart')
        self.line_edit_order_total = self.findChild(QLineEdit, 'line_edit_order_total')
        self.push_button_confirm = self.findChild(QPushButton, 'push_button_confirm')

        # Operations
        self.push_button_confirm.clicked.connect(self.func_confirm_order)

        # Initializers
        self.func_fill_cart()

        # show window
        self.show()

    def func_fill_cart(self):
        try:
            print('in function func_fill_cart')
            # fake data
            # my_order = Order()
            # my_order.set_order_id(1001)
            # my_order.set_customer(CompanyHandler.get_company_by_id(2))
            # my_order.add_product_to_cart(SoftwareHandler.get_software_by_id(8))
            # my_order.add_product_to_cart(SoftwareHandler.get_software_by_id(2))

            items_list = LoginScreen.current_order.get_items_list()
            print('count items in list = ', len(items_list))

            # Fill the table
            self.table_cart.setRowCount(len(items_list))
            row = 0
            for item in items_list:
                self.table_cart.setItem(row, 0, QTableWidgetItem( str(item.get_line_num()) ))
                self.table_cart.setItem(row, 1, QTableWidgetItem(item.get_product().get_product_name()))
                self.table_cart.setItem(row, 2, QTableWidgetItem(str(item.calc_unit_price())))
                self.table_cart.setItem(row, 3, QTableWidgetItem(str(item.get_quantity())))
                self.table_cart.setItem(row, 4,QTableWidgetItem( str(item.calc_item_total())))
                row += 1

            self.line_edit_order_total.setText(str(LoginScreen.current_order.get_order_total()))
        except Exception as ex:
            print('Error in func_fill_cart', ex)

    def func_confirm_order(self):
        msg = QMessageBox(self)
        result = msg.question(self, 'Confirm Order', 'Are you sure to confirm this order ?', msg.Yes | msg.No | msg.Cancel)
        if result == msg.Yes:
            OrderHandler.confirm_order(LoginScreen.current_order)
            self.func_save()
            # reset the order
            LoginScreen.current_order.get_items_list().clear()
            OrderItem.static_line_num = 1
            self.func_fill_cart()

    def func_save(self):
        try:
            msg = QMessageBox(self)
            msg.setText('Data Saved Successfully')
            msg.setWindowTitle('Saving..')
            msg.setIcon(QMessageBox.Information)
            msg.exec()
        except Exception as ex:
            print('Error in func add row', ex)

# main program
# app_object = QApplication(sys.argv) # sys.argv : list of parameters used when open window from terminal [ not often ]
# widgets_window_object = CartScreen()
# sys.exit(app_object.exec())  # exit screen only when user take action

