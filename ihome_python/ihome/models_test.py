import unittest
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from ihome.models import User


class DatabaseTest(unittest.TestCase):
# class DatabaseTest:
    def setUp(self):
        app = Flask(__name__)


        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://jw:7709@172.16.177.160:3306/ihome_python"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        self.app = app

        global db
        db = SQLAlchemy(app)

        # self.db = db
        # db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_user_model(self):
        # id = db.Column(db.Integer, primary_key=True)
        # name = db.Column(db.String(32), unique=True, nullable=False)
        # password_hash = db.Column(db.String(128), unique=True, nullable=False)
        # mobile = db.Column(db.String(11), unique=True, nullable=False)
        # real_name = db.Column(db.String(32))
        # id_card = db.Column(db.String(20))
        # # 用户头像路径
        # avatar_url = db.Column(db.String(128))
        #
        # # 在一表中，或者多表中写relationship
        # houses = db.relationship('House', backref='user')
        # orders = db.relationship('Order', backref='user')


        # user1 = User(name='jj', password_hash='111', mobile='18701068319',
        #              real_name='jw', id_card='18701068319')
        # user2 = User(name='ww', password_hash='222', mobile='15901068319',
        #              real_name='jw', id_card='15901068319')

        # db.session.add_all([user1, user2])
        # db.session.commit()

        with self.app.app_context():

            print(User.query.all())

    def test_(self):
        pass


# if __name__ == '__main__':
#     t = DatabaseTest()
#     t.setUp()
#     t.test_user_model()
