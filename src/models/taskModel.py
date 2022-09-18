from dataclasses import fields
from flask_restx import fields

from src.server.instance import server

task = server.api.model('Task', {
    'id': fields.String(description='O ID do registro.'),
    'name': fields.String(required=True, min_Length=1, max_Length=200,description='O Nome do registro.'),
    'description': fields.String(required=False, min_Length=1, max_Length=250,description='O descrição do registro.'),
    'Status': fields.String(required=False, min_Length=1, max_Length=250,description='O descrição do registro.')
})