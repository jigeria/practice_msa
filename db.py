import psycopg2
import traceback


class Databases:
    def __init__(self, host: str = "localhost", port: int = 5432):
        self.db = None
        self.db = psycopg2.connect(
            host=host,
            dbname="parksangmin",
            user="parksangmin",
            password="1234",
            port=port,
        )
        print("DB sucess")
        print("----Exception----")

        print("port: ", port)
        self.cursor = self.db.cursor()

    # def __del__(self):
    #     self.db.close()
    #     self.cursor.close()

    # def execute(self, query, args={}):
    #     self.cursor.execute(query, args)
    #     row = self.cursor.fetchall()
    #     return row

    # def commit(self):
    #     self.db.commit()
