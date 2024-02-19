from products.product import Product
from taxable.taxable import Taxable


class Hardware(Product, Taxable):
    def __init__(self,  product_id, product_name, product_retail_price, product_description, warranty_period):
        super().__init__(product_id, product_name, product_retail_price, product_description)
        self.__warranty_period = warranty_period

    # accessors
    def get_warranty_period(self):
        return self.__warranty_period

    def set_warranty_period(self, warranty_period):
        self.__warranty_period = warranty_period


    # override the abstract method get_tax() from Taxable class
    def get_tax(self, amount):
        return amount * Taxable.VAT_PERCENTAGE / 100


