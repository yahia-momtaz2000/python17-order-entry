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
        # 1- create db connection
        conn = DBConnectionFactory.create_connection()

        # 2- prepare sql statement
        sql = ('update products'
               ' set product_name = %s,'
               ' product_retail_price = %s,'
               ' product_desc = %s'
               ' where product_id = %s')

        # 3- set parameters
        values = (software.get_product_name(), software.get_product_retail_price(),
                  software.get_product_description(), software.get_product_id())

        # 4- execute sql statement
        my_cursor = conn.cursor()
        my_cursor.execute(sql, values)

        # Again to software table
        sql = ('update software'
               ' set software_licence = %s'
               ' where product_id = %s')

        values = (software.get_licence(), software.get_product_id())
        my_cursor.execute(sql, values)

        # 5- commit changes
        conn.commit()

    @staticmethod
    def delete_software(product_id):
        # 1- create db connection
        conn = DBConnectionFactory.create_connection()

        # 2- prepare sql statement
        sql = ('delete from software'
               ' where product_id = %s')

        # 3- set parameters
        values = (product_id, )

        # 4- execute statement
        my_cursor = conn.cursor()
        my_cursor.execute(sql, values)

        # again in products table
        sql = ('delete from products'
               ' where product_id = %s')

        values = (product_id, )
        my_cursor.execute(sql, values)

        # 5- Commit changes
        conn.commit()


    @staticmethod
    def get_all_software():

        software_list = []
        db_conn = None
        try:
            # 1- create db connection
            db_conn = DBConnectionFactory.create_connection()

            # 2- prepare sql statements
            sql_statement = ('SELECT products.PRODUCT_ID, PRODUCT_NAME, PRODUCT_RETAIL_PRICE, '
                             ' PRODUCT_DESC, SOFTWARE_LICENCE'
                             ' FROM products, software '
                             ' where products.PRODUCT_ID = software.PRODUCT_ID')

            # 3- execute statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement)

            # 4- Fetch all row
            rows = my_cursor.fetchall()

            # 5-  process ( loop ) each row and create software objects, append to List
            for row in rows:
                product_id = row[0]
                product_name = row[1]
                product_retail_price = row[2]
                product_description = row[3]
                software_licence = row[4]

                # Create a software object
                software = Software(product_id, product_name, product_retail_price, product_description, software_licence )

                # Append to sw list
                software_list.append(software)
        except mysql.connector.Error as ex:
            print('Error in insert function', ex)
        finally:
            # close db connection ( clean resource )
            if db_conn is not None:
                db_conn.close()

        return software_list

    @staticmethod
    def get_software_by_id(product_id):
        software = None
        db_conn = None
        try:
            # 1- create db connection
            db_conn = DBConnectionFactory.create_connection()
            # 2- prepare sql statement
            sql_statement = ('SELECT products.PRODUCT_ID, PRODUCT_NAME, PRODUCT_RETAIL_PRICE, '
                             ' PRODUCT_DESC, SOFTWARE_LICENCE'
                             ' FROM products, software '
                             ' where products.PRODUCT_ID = software.PRODUCT_ID'
                             ' and products.PRODUCT_ID = %s')
            # 3- set parameters
            values_tuple = (product_id, )
            # 4- execute statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement, values_tuple)
            # 5- Fetch a row
            row = my_cursor.fetchone()
            # 6- if row exists: create software object
            if row is not None:
                product_id = row[0]
                product_name = row[1]
                product_retail_price = row[2]
                product_description = row[3]
                software_licence = row[4]

                # create software object
                software = Software(product_id, product_name, product_retail_price,
                                    product_description, software_licence)

        except mysql.connector.Error as ex:
            print('Error in insert function', ex)
        finally:
            # close db connection ( clean resource )
            if db_conn is not None:
                db_conn.close()

        return software



# main program
# my_software = Software(product_name='Firefox', product_retail_price=300, product_description='browsers'
#                        , licence='512-12321-123-123')
# SoftwareHandler.insert_software(my_software)

# my_software = Software(8, product_name='Norton', product_retail_price=333, product_description='anti'
#                         , licence='555-222-333')
# SoftwareHandler.update_software(my_software)

# SoftwareHandler.delete_software(20)

# sw_list = SoftwareHandler.get_all_software()
# for software in sw_list:
#     print('product id = ', software.get_product_id())
#     print('product name = ', software.get_product_name())
#     print('product retail price = ', software.get_product_retail_price())
#     print('product desc = ', software.get_product_description())
#     print('sw licence = ', software.get_licence())
#     print('----')

# my_software = SoftwareHandler.get_software_by_id(15)
# print('product id = ', my_software.get_product_id())
# print('product name = ', my_software.get_product_name())
# print('product retail price = ', my_software.get_product_retail_price())
# print('product desc = ', my_software.get_product_description())
# print('sw licence = ', my_software.get_licence())