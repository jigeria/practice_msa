import json

from flask import Flask
from flask_restx import Api, Resource

from db import Databases

app = Flask(__name__)
api = Api(app)


USER_NAME = "sangmin"
TABLE_NAME = "CARD_INFO"


@api.route("/card")
class ReadCardDb(Resource):
    def get(self):
        db = Databases(host="db", port=5432)

        sql = f"SELECT * from {TABLE_NAME} WHERE user_name='{USER_NAME}';"
        db.cursor.execute(sql)
        result = db.cursor.fetchall()

        print("result: ", result)

        return {
            "user_id": json.dumps(result[0][0]),
            "user_name": json.dumps(result[0][1]),
            "card_number": json.dumps(result[0][2]),
        }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5200)
