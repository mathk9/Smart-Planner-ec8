from dataclasses import fields
from flask_restx import fields

from src.server.instance import server

user = server.api.model('User', {
    'id': fields.Integer(description='O ID do registro.'),
    'name': fields.String(required=True, min_Length=1, max_Length=200,description='O Nome do registro.')
})