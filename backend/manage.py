from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from plannerapi.application import create_app
from plannerapi.models import db, Planner, Card, Task

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# python contexto
@manager.shell
def shell_ctx():
    return dict(app=app,
                db=db,
                Planner=Planner,
                Card=Card,
                Task=Task)

if __name__ == '__main__':
    manager.run()