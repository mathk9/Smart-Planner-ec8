from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    planner = db.relationship('Planner', backref="creator", lazy=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password, method='sha256')

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        print('email: '+email + ' - password: ' +password)
        if not email or not password:
            return None

        user = cls.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def to_dict(self):
        return dict(id=self.id, email=self.email)

class Planner(db.Model):
    __tablename__ = 'planners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    cards = db.relationship('Card', backref="planner", lazy=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    cards=[card.to_dict() for card in self.cards])

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    planner_id = db.Column(db.Integer, db.ForeignKey('planners.id'))
    tasks = db.relationship('Task', backref='card', lazy=False)

    def to_dict(self):
        return dict(id=self.id,
                    text=self.text,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    planner_id=self.planner_id,
                    tasks=[task.to_dict() for task in self.tasks])

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    selected = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))

    def to_dict(self):
        return dict(id=self.id,
                    text=self.text,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    card_id=self.card_id)