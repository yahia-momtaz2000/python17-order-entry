from customers.customer import Customer


class Company(Customer):
    def __init__(self, customer_id=None, customer_name=None, customer_phone=None, customer_address=None,
                 contact=None, discount=None):
        super().__init__(customer_id, customer_name, customer_phone, customer_address)
        self.__contact = contact
        self.__discount = discount


    # accessors [ Getters & setters ]
    def get_contact(self):
        return self.__contact

    def get_discount(self):
        return self.__discount

    
