import unittest
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from ihome.models import *


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
        #db.create_all()


    def tearDown(self):
        db.session.remove()
        # db.drop_all()


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

            # print(User.query.all())
            # print(User.query.filter_by(name='jj').options('houses').all())
            # print(User.query.foreign())
            # print(User.query.filter_by(name='jj').first().houses)
            for h in User.query.filter_by(name='jj').first().houses:
                print('user:', h.user_id, h.title, end=',')


    def test_area_model(self):
        # area1 = Area(name='haidian')
        # area2 = Area(name='cangping')
        # db.session.add_all([area1, area2])
        # db.session.commit()
        with self.app.app_context():
            print('area:', Area.query.filter_by(name='haidian').first().houses)
        pass


    def test_house_model(self):
        # house1 = House(user_id=1, area_id=1, title='house1')
        # house2 = House(user_id=1, area_id=1, title='house2')
        # house3 = House(user_id=2, area_id=2, title='house3')
        # house4 = House(user_id=2, area_id=2, title='house4')
        # db.session.add_all([house1, house2, house3, house4])
        # db.session.commit()
        with self.app.app_context():
            print('house:', House.query.filter_by(user_id=2, area_id=2).first())
            pass

    def test_order_model(self):
        # order1 = Order(user_id=1, house_id=1,
        #                begin_date=datetime.datetime.now(),
        #                end_date=datetime.datetime.now(),
        #                days=3,
        #                house_price=200,
        #                amount=600)
        # order2 = Order(user_id=1, house_id=2,
        #                begin_date=datetime.datetime.now(),
        #                end_date=datetime.datetime.now(),
        #                days=3,
        #                house_price=200,
        #                amount=600)
        # order3 = Order(user_id=2, house_id=3,
        #                begin_date=datetime.datetime.now(),
        #                end_date=datetime.datetime.now(),
        #                days=3,
        #                house_price=200,
        #                amount=600)
        # order4 = Order(user_id=2, house_id=4,
        #                begin_date=datetime.datetime.now(),
        #                end_date=datetime.datetime.now(),
        #                days=3,
        #                house_price=200,
        #                amount=600)
        # db.session.add_all([order2, order3, order4])
        # db.session.commit()

        with self.app.app_context():
            print('order:', Order.query.filter_by(user_id=1, house_id=2).first())
            pass



# if __name__ == '__main__':
#     t = DatabaseTest()
#     t.setUp()
#     t.test_user_model()
