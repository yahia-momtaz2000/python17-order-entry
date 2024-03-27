# install packages   [ mysql - mysql-connector-python ]
import sys
import mysql.connector
class DBConnectionFactory:
    # static variables
    USER = 'root'
    PASSWORD = 'root'
    HOST = 'localhost'
    DATABASE = 'oe'

    @staticmethod
    def create_connection():
        db_conn = None
        try:
            db_conn = mysql.connector.connect(user=DBConnectionFactory.USER,
                                    password=DBConnectionFactory.PASSWORD,
                                    host=DBConnectionFactory.HOST,
                                    database=DBConnectionFactory.DATABASE)

            db_conn.autocommit = False
            print('db connection successful')
        except mysql.connector.Error as ex:
            print('DB Connection Failed', ex)
            sys.exit()
        return db_conn


# main program
# try the db connection
my_conn = DBConnectionFactory.create_connection()
print(my_conn)
