import psycopg2
import traceback


class Databases:
    def __init__(self, port: int = 5432):
        try:
            self.db = psycopg2.connect(
                host="postgres",
                dbname="parksangmin",
                user="parksangmin",
                password="1234",
                port=port,
            )
        except Exception as e:
            print(traceback.format_exc())
            print("Error: ", e)

        print("port: ", port)
        print("self.db: ", self.db)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()
