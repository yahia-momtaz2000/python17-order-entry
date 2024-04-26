from products.product import Product


class Software(Product):
    def __init__(self, product_id=None, product_name=None, product_retail_price=None, product_description=None, licence=None):
        super().__init__(product_id, product_name, product_retail_price, product_description)
        self.__licence = licence

    # Accessors
    def get_licence(self):
        return self.__licence

    def set_licence(self, licence):
        self.__licence = licence

