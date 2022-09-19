from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server
from src.models.medicalRecordModel import medicalRecord

app, api = server.app, server.api

medicalRecords_db = [
    {'id': 0, 'name': 'Cardiologista',
    'description': 'Ficha feita em 05/09, Dr. Mario',
    'content': 'Transplantado, infarto',
    'user': 1},
]

ITEM_NOT_FOUND = "Medical Record not found."

@api.route('/v1.0/medicalRecord/<int:id>')
class MedicalRecord(Resource):
    @api.doc('Get a Medical Record')
    def get(self, id):
        for i in range(len(medicalRecords_db)):
            if medicalRecords_db[i]['id'] == id:
                return medicalRecords_db[i]
        return {'message': ITEM_NOT_FOUND}, 404

    @api.doc('Delete an Medical Record')
    def delete(self, id):
        for i in range(len(medicalRecords_db)):
            if medicalRecords_db[i]['id'] == id:
                del medicalRecords_db[i]
                return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @api.expect(medicalRecord, validate=True)
    def put(self, id):
        response = api.payload
        for i in range(len(medicalRecords_db)):
            if medicalRecords_db[i]['id'] == id:
                medicalRecords_db[i] = response
                return medicalRecords_db[i], 200
        medicalRecords_db.append(response)
        return response, 200

@api.route('/v1.0/medicalRecords')
class MedicalRecordlist(Resource):
    @api.doc('Get all Medical Record')
    @api.marshal_list_with(medicalRecord)
    def get(self):
        return medicalRecords_db

    @api.expect(medicalRecord, validate=True)
    def post(self):
        response = api.payload
        medicalRecords_db.append(response)
        return response, 200        