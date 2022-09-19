from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server
from src.models.usersModel import user

app, api = server.app, server.api

users_db = [
    {'id': 0, 'name': 'Matheus'},
    {'id': 1, 'name': 'Ysabela'},
    {'id': 2, 'name': 'Caio'},
    {'id': 3, 'name': 'Giovana'},
]

ITEM_NOT_FOUND = "User not found."

@api.route('/v1.0/user/<int:id>')
class User(Resource):
    @api.doc('Get an User')
    def get(self, id):
        for i in range(len(users_db)):
            if users_db[i]['id'] == id:
                return users_db[i]
        return {'message': ITEM_NOT_FOUND}, 404

    @api.doc('Delete an User')
    def delete(self, id):
        for i in range(len(users_db)):
            if users_db[i]['id'] == id:
                del users_db[i]
                return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @api.expect(user, validate=True)
    def put(self, id):
        response = api.payload
        for i in range(len(users_db)):
            if users_db[i]['id'] == id:
                users_db[i] = response
                return users_db[i], 200
        users_db.append(response)
        return response, 200

@api.route('/v1.0/users')
class Userlist(Resource):
    @api.doc('Get all Users')
    @api.marshal_list_with(user)
    def get(self):
        return users_db

    @api.expect(user, validate=True)
    def post(self):
        response = api.payload
        users_db.append(response)
        return response, 200        