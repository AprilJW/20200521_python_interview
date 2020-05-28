from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from ihome import create_app
from ihome import db

app = create_app('develop')
# manage = Manager(app)
# Migrate(app, db)
# manage.add_command('db', MigrateCommand)




if __name__ == '__main__':
    # manage.run()
    app.run(debug=True)