import mysql.connector

from db.db_connection_factory import DBConnectionFactory
from products.software import Software


class SoftwareHandler:
    @staticmethod
    def insert_software(software):
        db_conn = None
        try:
            # steps for products table
            # 1 - create db connection
            db_conn = DBConnectionFactory.create_connection()

            # 2- prepare sql statement
            sql_statement = ('insert into products'
                             ' (PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC)'
                             ' values'
                             ' (%s, %s, %s)')

            # 3- set parameters
            values_tuple = (software.get_product_name(), software.get_product_retail_price()
                            , software.get_product_description())

            # 4- Create cursor and execute sql statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement, values_tuple)

            # Again the steps for software
            # Retrieve the last product id inserted
            v_last_product_id = my_cursor.lastrowid
            sql_statement = ('insert into software'
                             ' (SOFTWARE_LICENCE, PRODUCT_ID)'
                             ' values'
                             ' (%s, %s)')

            values_tuple = (software.get_licence(), v_last_product_id)
            my_cursor.execute(sql_statement, values_tuple)

            # 5- commit changes
            db_conn.commit()
        except mysql.connector.Error as ex:
            print('Error in insert function', ex)
        finally:
            # close db connection ( clean resource )
            if db_conn is not None:
                db_conn.close()
    @staticmethod
    def update_software(software):
        pass

    @staticmethod
    def delete_software(product_id):
        pass

    @staticmethod
    def get_all_software():
        pass

    @staticmethod
    def get_software_by_id(product_id):
        pass


# main program
my_software = Software(product_name='Firefox', product_retail_price=300, product_description='browsers'
                       , licence='512-12321-123-123')
SoftwareHandler.insert_software(my_software)

