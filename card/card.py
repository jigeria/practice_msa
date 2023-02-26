import json

from flask import Flask
from flask_restx import Api, Resource

from postgresql import CRUD

app = Flask(__name__)
api = Api(app)


@api.route("/card")
class ReadCardDb(Resource):
    def get(self):
        db = CRUD()
        result = db.readDB(table="CARD_INFO", colum="USER_ID, CARD_NUMBER")
        print("result: ", result[0], type(result[0]))

        return {
            "USER_ID": json.dumps(result[0][0]),
            "CARD_NUMBER": json.dumps(result[0][1]),
        }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5200)
