# import QtGui module from PyQt5 package
import sys
from PyQt5 import QtGui, uic
# from QtWidgets found in package PyQt5 import classes QApplication - QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, \
    QRadioButton, QCheckBox, QTextEdit, QMenu, QAction, QMdiArea, QTableWidget, QTableWidgetItem

from products.software import Software
from products.software_handler import SoftwareHandler


class SoftwareScreen(QMainWindow):  # inheritance FirstWindow class inherit from QMainWindow class
    def __init__(self):
        super().__init__()

        # Load ui File
        uic.loadUi('software_module_ui.ui', self)

        # Define Widgets
        # LineEdit widgets
        self.line_edit_product_id = self.findChild(QLineEdit, 'line_edit_product_id')
        self.line_edit_product_name = self.findChild(QLineEdit, 'line_edit_product_name')
        self.line_edit_product_price = self.findChild(QLineEdit, 'line_edit_product_price')
        self.line_edit_product_desc = self.findChild(QLineEdit, 'line_edit_product_desc')
        self.line_edit_product_licence = self.findChild(QLineEdit, 'line_edit_product_licence')

        # buttons widgets
        self.button_add = self.findChild(QPushButton, 'button_add')
        self.button_edit = self.findChild(QPushButton, 'button_edit')
        self.button_delete = self.findChild(QPushButton, 'button_delete')
        self.button_reset = self.findChild(QPushButton, 'button_reset')
        self.button_add_cart = self.findChild(QPushButton, 'button_add_cart')

        # table widget
        self.table_software = self.findChild(QTableWidget, 'table_software')

        # Define Operations
        self.button_add.clicked.connect(self.func_add_row)
        self.button_reset.clicked.connect(self.func_reset_data)
        self.table_software.clicked.connect(self.func_choose_row)
        self.button_edit.clicked.connect(self.func_edit_row)
        self.button_delete.clicked.connect(self.func_delete_row)

        # Initializers
        # Load table data
        self.func_load_data()

        # show window
        self.show()

    def func_load_data(self):
        try:
            print('func load data')
            # 1. Retrieve data from software handler [ get all software function ] to a list
            software_list = SoftwareHandler.get_all_software()
            print('Software count = ', len(software_list))

            # 2. Loop over the list and fill the table widget
            self.table_software.setRowCount(len(software_list))
            row = 0
            for software in software_list:
                # object from class QTableWidgetItem
                self.table_software.setItem(row, 0, QTableWidgetItem(str(software.get_product_id())))
                self.table_software.setItem(row, 1, QTableWidgetItem(software.get_product_name()))
                self.table_software.setItem(row, 2, QTableWidgetItem(str(software.get_product_retail_price())))
                self.table_software.setItem(row, 3, QTableWidgetItem(software.get_product_description()))
                self.table_software.setItem(row, 4, QTableWidgetItem(software.get_licence()))
                row += 1
        except Exception as msg:
            print('Error in func load data ', msg)

    def func_add_row(self):
        try:
            # 1 read data from line edit fields
            # product_id = self.line_edit_product_id.text()
            product_name = self.line_edit_product_name.text()
            product_retail_price = self.line_edit_product_price.text()
            product_description = self.line_edit_product_desc.text()
            product_licence = self.line_edit_product_licence.text()

            # 2 insert() from handler
            my_software = Software(product_name=product_name,
                                   product_retail_price= product_retail_price,
                                   product_description = product_description,
                                   licence=product_licence)
            SoftwareHandler.insert_software(my_software)

            # 3 again call func_load_data to fill table widget again
            self.func_load_data()

            # 4 reset data
            self.func_reset_data()

            # save dialog
            self.func_save()
        except Exception as ex:
            print('Error in func add row', ex)

    def func_choose_row(self):
        try:
            # 1. find the current selected row
            current_selected_row = self.table_software.currentRow()

            # 2. fill variables from the current row
            product_id = self.table_software.item(current_selected_row, 0).text()
            product_name = self.table_software.item(current_selected_row, 1).text()
            product_retail_price = self.table_software.item(current_selected_row, 2).text()
            product_description = self.table_software.item(current_selected_row, 3).text()
            product_licence = self.table_software.item(current_selected_row, 4).text()

            # 3. fill line edit fields with these variables
            self.line_edit_product_id.setText(str(product_id))
            self.line_edit_product_name.setText(product_name)
            self.line_edit_product_price.setText(str(product_retail_price))
            self.line_edit_product_desc.setText(product_description)
            self.line_edit_product_licence.setText(product_licence)
        except Exception as ex:
            print('Error in choose row func', ex)

    def func_edit_row(self):
        # 1. read data from line edit product id > licence
        product_id = self.line_edit_product_id.text()
        product_name = self.line_edit_product_name.text()
        product_retail_price = self.line_edit_product_price.text()
        product_description = self.line_edit_product_desc.text()
        product_licence = self.line_edit_product_licence.text()

        # 2. create object from software and use handler > update()
        my_software = Software(product_id=product_id,
                               product_name=product_name,
                               product_retail_price=product_retail_price,
                               product_description=product_description,
                               licence=product_licence)
        SoftwareHandler.update_software(my_software)

        # 3. reload data into software widget table
        self.func_load_data()
        # 4. save dialog
        self.func_save()
        # 5. reset data
        self.func_reset_data()

    def func_delete_row(self):
        # 0. Question QMessageBox
        msg = QMessageBox(self)
        result = msg.question(self, 'deleting', 'Are you sure to delete this record ?', msg.Yes | msg.No | msg.Cancel)
        if result == msg.Yes:
            # 1. read product id from line edit
            product_id = self.line_edit_product_id.text()

            # 2. software handler > delete function ()
            SoftwareHandler.delete_software(product_id)

            # 3. load data > remove the current row from table widget
            current_selected_row = self.table_software.currentRow()
            self.table_software.removeRow(current_selected_row)

            # 4. save dialog
            self.func_save()
            # 5. reset data
            self.func_reset_data()

    def func_reset_data(self):
        try:
            self.line_edit_product_id.setText('')
            self.line_edit_product_name.setText('')
            self.line_edit_product_price.setText('')
            self.line_edit_product_desc.setText('')
            self.line_edit_product_licence.setText('')
        except Exception as ex:
            print('Error in func add row', ex)

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
# widgets_window_object = SoftwareScreen()
# sys.exit(app_object.exec())  # exit screen only when user take action

