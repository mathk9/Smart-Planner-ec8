from dataclasses import fields
from flask_restx import fields

from src.server.instance import server

medicalRecord = server.api.model('Medical Record', {
    'id': fields.Integer(description='O ID do registro.'),
    'name': fields.String(required=True, min_Length=1, max_Length=200,description='O Nome do registro.'),
    'description': fields.String(required=False, min_Length=1, max_Length=250,description='O descrição do registro.'),
    'content': fields.String(required=False, min_Length=1, max_Length=3000,description='O descrição do registro.'),
    'user': fields.String(description='O ID do usuário'),
})