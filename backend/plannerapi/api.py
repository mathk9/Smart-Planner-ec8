from functools import wraps
from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request, current_app

import jwt

from plannerapi.models import db, Planner, Card, Task, User

api = Blueprint('api', __name__)

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.filter_by(email=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify


@api.route('/register/', methods=('POST',))
def register():
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@api.route('/login/', methods=('POST',))
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401

    token = jwt.encode({
        'sub': user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    print('token: '+ token.decode('UTF-8'))
    return jsonify({ 'token': token.decode('UTF-8') })


@api.route('/planners/', methods=('POST',))
@token_required
def create_planner(current_user):
    data = request.get_json()
    planner = Planner(name=data['name'])
    cards = []
    for q in data['cards']:
        card = Card(text=q['card'])
        card.tasks = [Task(text=c) for c in q['tasks']]
        cards.append(card)
    planner.cards = cards
    planner.creator = current_user
    db.session.add(planner)
    db.session.commit()
    return jsonify(planner.to_dict()), 201


@api.route('/planners/', methods=('GET',))
def fetch_planners():
    planners = Planner.query.all()
    return jsonify([s.to_dict() for s in planners])


@api.route('/planners/<int:id>/', methods=('GET', 'PUT'))
def planner(id):
    if request.method == 'GET':
        planner = Planner.query.get(id)
        return jsonify(planner.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        for q in data['cards']:
            task = Task.query.get(q['task'])
            task.selected = task.selected + 1
        db.session.commit()
        planner = Planner.query.get(data['id'])
        return jsonify(planner.to_dict()), 201
