from flask_restful import Resource, request
from .models import UserModel, PostModel, CommentModel
from .schemas import UserSchema, PostSchema, CommentSchema


class AllUsersResource(Resource):
    def get(self):
        users = UserModel.query.all()
        schema = UserSchema()
        dump = schema.dump(users, many=True)
        return dump, 200


class AllPostsResource(Resource):
    def get(self):
        posts = PostModel.query.all()
        schema = PostSchema()
        dump = schema.dump(posts, many=True)
        return dump, 200


class AllCommentsResource(Resource):
    def get(self):
        comments = CommentModel.query.all()
        schema = CommentSchema()
        dump = schema.dump(comments, many=True)
        return dump, 200


class UserResource(Resource):
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        schema = UserSchema()
        dump = schema.dump(user)
        return dump, 200

    def post(self):
        req = request.get_json()
        schema = UserSchema()
        errors = schema.validate(req)
        if errors:
            return {'errors': errors}
        data = schema.dump(req)
        print(data)
        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'User successfully created'}, 201

    def patch(self, user_id):
        UserModel.update_by_id(user_id, **request.form)
        return {'message:': f'User with id:{user_id} successfully updated'}, 200

    def delete(self, user_id):
        UserModel.delete_by_id(user_id)
        return {'message': f'User with id:{user_id} successfully deleted'}, 200


class PostResource(Resource):
    def get(self, post_id):
        post = PostModel.query.get(post_id)
        schema = PostSchema()
        dump = schema.dump(post)
        return dump, 200


class CommentResource(Resource):
    def get(self, comment_id):
        comment = CommentModel.query.get(comment_id)
        schema = CommentSchema()
        dump = schema.dump(comment)
        return dump, 200
