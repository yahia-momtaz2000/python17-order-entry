from datetime import datetime

from orders.order_item import OrderItem

class Order:
    def __init__(self, order_id, customer):
        self.__order_id = order_id
        self.__customer = customer
        self.__order_date = datetime.now()
        self.__order_total = 0.0
        self.__items_list = []

    # accessors
    def get_order_total(self):
        sum_total = 0
        for item in self.__items_list:
            sum_total = sum_total + item.calc_item_total()
            self.__order_total = sum_total
        return self.__order_total


    # extra methods
    def print_order_receipt(self):
        print('------------------ Order data -----------------')
        print('Order id = ', self.__order_id)
        print('Customer name = ', self.__customer.get_customer_name())
        print('Order date = ', self.__order_date.date())
        print('Order Total = ', self.get_order_total())
        print('------------------- Order Items List Lines --------------------')
        for item in self.__items_list:
            print('line nbr = ', item.get_line_num())
            print('Product name = ', item.get_product().get_product_name())
            print('Quantity = ', item.get_quantity())
            print('Unit price = ', item.calc_unit_price())
            print('item tax = ', item.calc_item_tax())
            print('item total = ', item.calc_item_total())
            print('--------------')


    def add_product_to_cart(self, new_product):  # append new_product to items_list ( list of order items lines )
        # check if product already exist in the list or not
        is_found = False
        for item in self.__items_list:
            if new_product.get_product_id() == item.get_product().get_product_id():
                current_quantity = item.get_quantity()
                item.set_quantity(current_quantity + 1)
                is_found = True

        if is_found == False:
        # create new object from OrderItem class
            new_item_line = OrderItem(new_product, 1)
            self.__items_list.append(new_item_line)