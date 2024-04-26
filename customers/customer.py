from abc import ABC


class Customer(ABC):
    # constructor
    def __init__(self, customer_id=None, customer_name=None, customer_phone=None, customer_address=None):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__customer_phone = customer_phone
        self.__customer_address = customer_address
    # Accessors [ Getters & setters ]
    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_customer_name(self):
        return self.__customer_name
    def get_customer_phone(self):
        return self.__customer_phone
    def get_customer_address(self):
        return self.__customer_address

    # Extra methods
