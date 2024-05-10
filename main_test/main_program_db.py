from customers.company import Company
from customers.company_handler import CompanyHandler
from orders.order import Order
from orders.order_handler import OrderHandler
from products.hardware import Hardware
from products.software import Software
from products.software_handler import SoftwareHandler

# 1. create objects from products ( Hw | Sw | Manual )
# keyboard = Hardware(1, "keyboard", 100, "accessories", 3)
office2028 = SoftwareHandler.get_software_by_id(2)
photoshop = SoftwareHandler.get_software_by_id(15)
# printer_canon = Hardware(3, "Canon printer", 500, "printers", 10)

# 2 . create object from customer ( Company | Individual )
raya = CompanyHandler.get_company_by_id(4)

# 3. create order object
my_order = Order(1002, raya)

# 4. add_product_to_cart more than once
my_order.add_product_to_cart(office2028)




# 5. print receipt ( preview )
my_order.print_order_receipt()

# 6- Add Order and order details to the db
OrderHandler.confirm_order(my_order)
