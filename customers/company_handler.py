from db.db_connection_factory import DBConnectionFactory


class CompanyHandler:
    @staticmethod
    def insert_company(company):
        # 1- create db connection
        db_conn = DBConnectionFactory.create_connection()

        pass

    @staticmethod
    def update_company(company):
        pass

    @staticmethod
    def delete_company(company_id):
        pass

    @staticmethod
    def select_all_companies():
        pass

    @staticmethod
    def select_company_by_id(company_id):
        pass