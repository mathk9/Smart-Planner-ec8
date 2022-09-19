from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server
from src.models.taskModel import task

app, api = server.app, server.api

tasks_db = [
    {'id': 0, 'name': 'Tomar café da manhã', 'description': 'Uva na geladeira', 'status': 'Em progresso'},
    {'id': 1, 'name': 'Escovar os dentes', 'description': 'Escova azul', 'status': 'Feito'},
    {'id': 2, 'name': 'Remédio Pressão', 'description': 'Capsula azul e branca, caixa 3', 'status': 'Não feito'},
]

ITEM_NOT_FOUND = "Task not found."

@api.route('/v1.0/task/<int:id>')
class Task(Resource):
    @api.doc('Get a Task')
    def get(self, id):
        for i in range(len(tasks_db)):
            if tasks_db[i]['id'] == id:
                return tasks_db[i]
        return {'message': ITEM_NOT_FOUND}, 404

    @api.doc('Delete an Task')
    def delete(self, id):
        for i in range(len(tasks_db)):
            if tasks_db[i]['id'] == id:
                del tasks_db[i]
                return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @api.expect(task, validate=True)
    def put(self, id):
        response = api.payload
        for i in range(len(tasks_db)):
            if tasks_db[i]['id'] == id:
                tasks_db[i] = response
                return tasks_db[i], 200
        tasks_db.append(response)
        return response, 200

@api.route('/v1.0/tasks')
class Tasklist(Resource):
    @api.doc('Get all Tasks')
    @api.marshal_list_with(task)
    def get(self):
        return tasks_db

    @api.expect(task, validate=True)
    def post(self):
        response = api.payload
        tasks_db.append(response)
        return response, 200        