from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
api = Api(app)
CORS(app)

from .resources import UserResource, PostResource, CommentResource, AllUsersResource, AllPostsResource, AllCommentsResource
api.add_resource(AllUsersResource, '/users')
api.add_resource(UserResource, '/user', '/user/<int:user_id>')
api.add_resource(AllPostsResource, '/posts')
api.add_resource(PostResource, '/post', '/post/<int:post_id>')
api.add_resource(AllCommentsResource, '/comments')
api.add_resource(CommentResource, '/comment', '/comment/<int:comment_id>')
