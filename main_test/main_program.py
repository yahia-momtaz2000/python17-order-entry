from customers.company import Company
from orders.order import Order
from products.hardware import Hardware
from products.software import Software

# 1. create objects from products ( Hw | Sw | Manual )
keyboard = Hardware(1, "keyboard", 100, "accessories", 3)
office2022 = Software(2, "office 2022", 200, "Ms Office", "554-65-211")
printer_canon = Hardware(3, "Canon printer", 500, "printers", 10)

# 2 . create object from customer ( Company | Individual )
raya = Company(100, "Raya Co.", "01012312312", "Cairo", "Ahmed Mostafa", 0.0)

# 3. create order object
my_order = Order(1002, raya)

# 4. add_product_to_cart more than once
my_order.add_product_to_cart(office2022)
my_order.add_product_to_cart(office2022)
my_order.add_product_to_cart(keyboard)
my_order.add_product_to_cart(keyboard)
my_order.add_product_to_cart(keyboard)


# 5. print receipt
my_order.print_order_receipt()
