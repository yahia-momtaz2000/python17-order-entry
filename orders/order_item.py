from products.hardware import Hardware


class OrderItem:
    # static attribute
    static_line_num = 1
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity
        self.__line_num = OrderItem.static_line_num
        OrderItem.static_line_num += 1

    def get_line_num(self):
        return self.__line_num

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    # Extra methods
    def calc_unit_price(self):
        return self.__product.get_product_retail_price()

    def calc_item_tax(self):
        if isinstance(self.__product, Hardware): # polymorphism oop concept
            amount = self.calc_unit_price() * self.__quantity
            return self.__product.get_tax( amount )
        else:
            return 0

    def calc_item_total(self):
        return self.calc_unit_price() * self.__quantity + self.calc_item_tax()
