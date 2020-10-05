from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
api = Api(app)

from .resources import UserResource
api.add_resource(UserResource, '/user', '/user/<int:user_id>')
