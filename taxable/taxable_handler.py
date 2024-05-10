from db.db_connection_factory import DBConnectionFactory


class TaxableHandler:
    @staticmethod
    def get_param_value(param_name):
        # 1- create db connection
        db_conn = DBConnectionFactory.create_connection()
        param_value = -1

        # 2- prepare sql statement
        sql_statement = ('SELECT param_value '
                         ' FROM parameters'
                         ' where param_name = %s')

        # 3- set parameters
        values_tuple = (param_name, )

        # 4- execute statement
        my_cursor = db_conn.cursor()
        my_cursor.execute(sql_statement, values_tuple)

        # 5- Fetch 1 row
        row = my_cursor.fetchone()

        # 6- if row exists - create object
        if row is not None:
            param_value = row[0]

        return param_value

    @staticmethod
    def update_param_value(param_name, param_value):
        # 1- create db connection
        db_conn = DBConnectionFactory.create_connection()

        # 2- prepare sql statement
        sql_statement = ('update parameters'
                         ' set param_value = %s'
                         ' where param_name = %s')

        # 3- set parameters
        values_tuple = (param_value, param_name)

        # 4- execute statement
        my_cursor = db_conn.cursor()
        my_cursor.execute(sql_statement, values_tuple)

        # 5- Commit changes
        db_conn.commit()



# main program
# param_val = TaxableHandler.get_param_value('VAT_PCT')
# print(param_val)


TaxableHandler.update_param_value(param_name='VAT_PCT', param_value=50)