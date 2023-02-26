from db import Databases


class CRUD(Databases):
    def insertDB(self, table):
        sql = f"INSERT INTO {table} VALUES (1,'sangmin','1234-5678-5592-2323');"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(" insert DB err ", e)

    def readDB(self, table, colum, where_key: str = None, where_condition: str = None):
        sql = f"SELECT {colum} from {table};"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        return result

    def updateDB(self, schema, table, colum, value, condition):
        sql = " UPDATE {schema}.{table} SET {colum}='{value}' WHERE {colum}='{condition}' ".format(
            schema=schema, table=table, colum=colum, value=value, condition=condition
        )
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(" update DB err", e)

    def deleteDB(self, schema, table, condition):
        sql = " delete from {schema}.{table} where {condition} ; ".format(
            schema=schema, table=table, condition=condition
        )
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("delete DB err", e)

    def initDB(self, table: str):
        sql = f"CREATE TABLE {table} (USER_ID SERIAL PRIMARY KEY, USERNAME VARCHAR(50) UNIQUE NOT NULL, CARD_NUMBER VARCHAR(50) NOT NULL ); "
        result = self.cursor.execute(sql)
        self.commit()

        return result


if __name__ == "__main__":
    table_name = "USER_ACCOUNT"
    db_column = ()
    db = CRUD()

    # db.initDB(table="USER_ACCOUNT")
    # db.insertDB(table=table_name)
    result = db.readDB(colum="USER_ID", table=table_name)
    print("result: ", result)
    # result = db.readDB(table="user_account", colum="USER_ID, USERNAME")
    # print('result: ', result[0], type(result[0]))
    # db.insertDB(schema='public',table='test',colum='user_id',data='test')
    # print(db.readDB(schema='public',table='test',colum='user_id'))
    # db.updateDB(schema='myschema',table='table',colum='ID', value='와우',condition='유동적변경')
    # db.deleteDB(schema='myschema',table='table',condition ="id != 'd'")
