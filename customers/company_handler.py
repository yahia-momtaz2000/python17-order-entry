import mysql.connector

from customers.company import Company
from db.db_connection_factory import DBConnectionFactory


class CompanyHandler:
    @staticmethod
    def insert_company(company):
        db_conn = None
        try:
            # 1- create db connection
            db_conn = DBConnectionFactory.create_connection()
            # 2- prepare sql statement ( insert statement )
            sql_statement = ('insert into customers'
                             ' (CUSTOMER_NAME, CUSTOMER_ADDRESS, CUSTOMER_PHONE,'
                             ' CUSTOMER_CONTACT, CUSTOMER_DISCOUNT, CUSTOMER_TYPE_ID)'
                             ' values'
                             ' (%s, %s, %s, %s, %s, 1)')      # placeholders
            # 3- set parameters ( data ) %s
            values_tuple = (company.get_customer_name(), company.get_customer_address(),
                            company.get_customer_phone(), company.get_contact(), company.get_discount())
            # 4- Create cursor, use parameters and execute sql statement
            my_cursor = db_conn.cursor()
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
    def update_company(company):
        # 1- create db connection
        db_conn = DBConnectionFactory.create_connection()

        # 2- prepare sql statement
        sql_statement = ('update customers'
                         ' set CUSTOMER_NAME = %s,'
                         ' CUSTOMER_ADDRESS = %s,'
                         ' CUSTOMER_PHONE = %s,'
                         ' CUSTOMER_CONTACT = %s,'
                         ' CUSTOMER_DISCOUNT = %s'
                         ' where CUSTOMER_ID = %s')

        # 3- set parameters [ place holders ]
        values_tuple = (company.get_customer_name(), company.get_customer_address(),
                        company.get_customer_phone(), company.get_contact(), company.get_discount(),
                        company.get_customer_id())

        # 4- Create cursor and execute sql statement
        my_cursor = db_conn.cursor()
        my_cursor.execute(sql_statement, values_tuple)

        # 5- Commit changes
        db_conn.commit()

    @staticmethod
    def delete_company(customer_id):
        # 1- create db connection
        db_conn = DBConnectionFactory.create_connection()

        # 2- prepare sql statement
        sql_statement = ('delete from customers '
                         ' where customer_id = %s'
                         ' and customer_type_id = 1')

        # 3- set parameters
        values_tuple = (customer_id, )

        # 4- Create cursor and execute sql statement
        my_cursor = db_conn.cursor()
        my_cursor.execute(sql_statement, values_tuple)

        # 5- Commit changes
        db_conn.commit()

    @staticmethod
    def get_all_companies():
        db_conn = None
        companies_list = []
        try:
            # 1- create db connection
            db_conn = DBConnectionFactory.create_connection()

            # 2- prepare sql statement - prepare a list
            sql_statement = ('select CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_ADDRESS, '
                             ' CUSTOMER_PHONE, CUSTOMER_CONTACT, CUSTOMER_DISCOUNT, CUSTOMER_TYPE_ID'
                             ' from customers'
                             ' where customer_type_id = 1'
                             ' order by CUSTOMER_DISCOUNT ASC')

            # 3- execute statement ( ignore set parameters step )
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement)

            # 4- Fetch all rows
            rows = my_cursor.fetchall()

            # 5- process ( loop ) each row and create customer objects, append to List
            for row in rows:
                # retrieve each row into variables
                customer_id = row[0]
                customer_name = row[1]
                customer_address = row[2]
                customer_phone = row[3]
                customer_contact = row[4]
                customer_discount = row[5]

                # Create company object
                my_company = Company(customer_id, customer_name, customer_phone, customer_address
                                     , customer_contact, customer_discount)

                # append object to the list
                companies_list.append(my_company)
        except mysql.connector.Error as ex:
            print('Error in get all companies function', ex)
        finally:
            # close db connection ( clean resource )
            if db_conn is not None:
                db_conn.close()
        # 6- return the List
        return companies_list

    @staticmethod
    def get_company_by_id(customer_id):
        db_conn = None
        my_company = None
        try:
            # 1- create db connection
            db_conn = DBConnectionFactory.create_connection()
            # 2- prepare sql statement
            sql_statement = ('select CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_ADDRESS, '
                             ' CUSTOMER_PHONE, CUSTOMER_CONTACT, CUSTOMER_DISCOUNT, CUSTOMER_TYPE_ID'
                             ' from customers'
                             ' where customer_type_id = 1'
                             ' and customer_id = %s')
            # 3- set parameters
            values_tuple = (customer_id, )
            # 4- execute statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement, values_tuple)
            # 5- Fetch One Row
            row = my_cursor.fetchone()
            # 6-  if row exists : create the object
            if row is not None:
                # retrieve row into variables
                customer_id = row[0]
                customer_name = row[1]
                customer_address = row[2]
                customer_phone = row[3]
                customer_contact = row[4]
                customer_discount = row[5]

                # Create company object
                my_company = Company(customer_id, customer_name, customer_phone, customer_address
                                     , customer_contact, customer_discount)
        except mysql.connector.Error as ex:
            print('Error in get all companies function', ex)
        finally:
            # close db connection ( clean resource )
            if db_conn is not None:
                db_conn.close()
        # return the object
        return my_company

# main program ( test case )
# test insert
# my_company = Company(customer_name='BTech', customer_phone='0116549879', customer_address='Alex',
#                      contact='Usama Ahmed', discount=18)
# CompanyHandler.insert_company(my_company)

# test update
# my_company = Company(customer_id=3, customer_name='Raya Co.', customer_phone='01001231231', customer_address='50 Maadi cairo',
#                      contact='Motafa Esam Erfan', discount=22)
# CompanyHandler.update_company(my_company)

# test delete
# CompanyHandler.delete_company(2)

# test get_all_companies()

# my_companies_list = CompanyHandler.get_all_companies()
# for company in my_companies_list:
#     print('customer id = ', company.get_customer_id())
#     print('customer name = ', company.get_customer_name())
#     print('customer phone = ', company.get_customer_phone())
#     print('customer address = ', company.get_customer_address())
#     print('customer contact = ', company.get_contact())
#     print('customer discount = ', company.get_discount())
#     print('-----')

# test get_company_by_id
# my_company = CompanyHandler.get_company_by_id(4)
# print('customer id = ', my_company.get_customer_id())
# print('customer name = ', my_company.get_customer_name())
# print('customer phone = ', my_company.get_customer_phone())
# print('customer address = ', my_company.get_customer_address())
# print('customer contact = ', my_company.get_contact())
# print('customer discount = ', my_company.get_discount())



# insert company
# my_company = Company(customer_name='Samsung', customer_phone='012312312312', customer_address='Zagazig',
#                      contact='Ahmed Hasan', discount=10)
# CompanyHandler.insert_company(my_company)

# delete company
CompanyHandler.delete_company(5)