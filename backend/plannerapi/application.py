from flask import Flask
from flask_cors import CORS

def create_app(app_name='PLANNER_API'):
    app = Flask(app_name)
    app.config.from_object('plannerapi.config.BaseConfig')

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    from plannerapi.api import api
    app.register_blueprint(api, url_prefix="/api")

    from plannerapi.models import db
    db.init_app(app)

    return app