from db.db_connection_factory import DBConnectionFactory


class OrderHandler:
    @staticmethod
    def confirm_order(order):
        # 1- Create db connection
        db_conn = DBConnectionFactory.create_connection()

        # 2- prepare sql statement
        sql_statement = ('insert into orders'
                         ' (ORDER_DATE, ORDER_TOTAL, CUSTOMER_ID)'
                         ' values'
                         ' (%s, %s, %s)')

        # 3- set parameters
        values_tuple = (order.get_order_date(), order.get_order_total(),
                        order.get_customer().get_customer_id())

        # 4- execute statement
        my_cursor = db_conn.cursor()
        my_cursor.execute(sql_statement, values_tuple)

        # Again steps for order items table through a loop
        last_order_id = my_cursor.lastrowid
        items_list = order.get_items_list()

        for item in items_list:
            # prepare sql statement
            sql_statement = ('insert into order_items'
                             ' (ORDER_ITEM_QTY, ORDER_ID, PRODUCT_ID)'
                             ' values'
                             ' (%s, %s, %s)')

            # set parameters
            values_tuple = (item.get_quantity(), last_order_id, item.get_product().get_product_id())

            # execute statement
            my_cursor.execute(sql_statement, values_tuple)

        # 5- Commit changes
        db_conn.commit()

