from abc import ABC


class Product(ABC):
    def __init__(self, product_id, product_name, product_retail_price, product_description):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_retail_price = product_retail_price
        self.__product_description = product_description

    # Accessors
    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, product_id):
        self.__product_id = product_id

