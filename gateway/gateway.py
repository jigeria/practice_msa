import json
import os

from requests import Response
from requests.sessions import Session, session
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


def get_info(url):
    session_: Session = session()
    response: Response = session_.get(url=url)
    if response.status_code != 200:
        raise ValueError("Bad credentials")

    return response.json()


@api.route("/data")
class GateWay(Resource):
    def get(self):
        # card_url: str = "https://card.jigeria.me/card"
        # user_url: str = "https://user.jigeria.me/user"
        user_url: str = "http://user_server:5101/user"
        card_url: str = "http://card_server:5102/card"

        user_info = get_info(user_url)
        card_info = get_info(card_url)
        print("user info: ", user_info)
        print("card info: ", card_info)

        return {
            "USER_ID": user_info["user_id"],
            "USERNAME": user_info["user_name"],
            "CARD_NUMBER": card_info["card_number"],
        }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5400)
