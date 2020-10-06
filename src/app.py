import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, redirect
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())
if os.getenv('CONFIG') == "local":
    from config.local_config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG, HOST_URL, DB_USER, DB_PASS, DB_URL, DB_NAME
elif os.getenv('CONFIG') == "test":
    from config.test_config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG, HOST_URL, DB_USER, DB_PASS, DB_URL, DB_NAME
elif os.getenv('CONFIG') == "docker":
    from config.docker_config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG, HOST_URL, DB_USER, DB_PASS, DB_URL, DB_NAME

app = Flask(__name__)

DB_URL = 'postgresql+psycopg2://{user}:{pswd}@{url}/{db}'.format(user=DB_USER, pswd=DB_PASS, url=DB_URL,
                                                                 db=DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

from controllers import links


@app.route('/long_to_short', methods=['POST'])
def long_to_short():
    req = request.get_json()
    if not req or "full_link" not in req:
        return {"error": "full_link not provided!"}, 432
    link = links.add(req["full_link"])
    short_link = "http://{domain}/{short_link_postfix}".format(domain=HOST_URL,
                                                               short_link_postfix=link["short_link_postfix"])
    return {"result": {"short_link": short_link}}, 200


@app.route('/<short_link_postfix>', methods=['GET'])
def get_short_link(short_link_postfix):
    link = links.get(short_link_postfix=short_link_postfix)
    if link:
        return redirect(link["full_link"], code=302)
    else:
        return {"error": "Invalid link postfix!"}, 404  # return 404 error page


@app.route('/statistics/<short_link_postfix>', methods=['GET'])
def get_statistic(short_link_postfix):
    statistic = links.get_statistic(short_link_postfix=short_link_postfix)
    if statistic:
        statistic.pop("id")
        statistic.pop("link_id")
        return {"result": {"statistic": statistic}}, 200
    else:
        return {"error": "Invalid link postfix!"}, 404  # return 404 error page


if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
