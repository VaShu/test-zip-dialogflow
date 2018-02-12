import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, Server
from app.models import Zip

from app import create_app, db

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(app, db, render_as_batch=True)
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Zip=Zip)


@manager.command
@manager.option('-t')
def test(test=None):
    """Run the unit tests."""
    import unittest
    if test:
        tests = unittest.TestLoader().discover('tests', pattern=test)
    else:
        tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command("run", Server(host="127.0.0.1", port=8888))


if __name__ == '__main__':
    manager.run()
