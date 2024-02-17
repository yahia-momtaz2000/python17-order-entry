from products.product import Product


class Software(Product):
    def __init__(self, product_id, product_name, product_retail_price, product_description, licence):
        super().__init__(product_id, product_name, product_retail_price, product_description)
        self.__licence = licence


    # Accessorrs
    def get_licence(self):
        return self.__licence

    def set_licence(self, licence):
        self.__licence = licence

