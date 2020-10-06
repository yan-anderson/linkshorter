# import os
#
# from dotenv import load_dotenv, find_dotenv
# from flask_marshmallow import Marshmallow
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
#
# from app import app
#
# load_dotenv(find_dotenv())
# if os.getenv('CONFIG') == "local":
#     from config.local_config import DB_USER, DB_PASS, DB_URL, DB_NAME
# elif os.getenv('CONFIG') == "test":
#     from config.test_config import DB_USER, DB_PASS, DB_URL, DB_NAME
#
# DB_URL = 'postgresql+psycopg2://{user}:{pswd}@{url}/{db}'.format(user=DB_USER, pswd=DB_PASS, url=DB_URL, db=DB_NAME)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
# db = SQLAlchemy(app)
# ma = Marshmallow(app)