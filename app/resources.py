from flask_restful import Resource, request
from .models import UserModel


class UserResource(Resource):
    def get(self):
        users = UserModel.query.all()
        return [user.json() for user in users], 200

    def post(self):
        user = UserModel(**request.form)
        user.save_to_db()
        return f'{user.name} saved to database', 201

    def put(self):
        return 'put request'

    def patch(self, user_id):
        UserModel.update_by_id(user_id, **request.form)
        return f'User with id:{user_id} successfully updated ', 200

    def delete(self, user_id):
        UserModel.delete_by_id(user_id)
        return f'User with id:{user_id} successfully deleted', 200
