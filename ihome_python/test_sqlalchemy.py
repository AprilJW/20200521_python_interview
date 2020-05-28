import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from ihome.models import Area, House, house_facility, Facility
import threading

# charset=armscii8

conn = create_engine("mysql+pymysql://jw:7709@172.16.177.160:3306/ihome_python",
                     )
ret = conn.execute("select * from ihome_python_area_info")
result = ret.fetchall()
# print(result)





# session
# session对象线程不安全。所以不同线程，应该使用不用的session对象。
# Session类和engine有一个就行了。

# 每次执行数据库操作的时候，都需要创建一个session,相当于管理器
egine = create_engine("mysql+pymysql://jw:7709@172.16.177.160:3306/ihome_python",
                     echo=False)
Session = sessionmaker(bind=egine)
# 线程安全，基于本地线程实现每个线程用同一个session
session = scoped_session(Session)




# area = Area(name='xicheng')
# area1 = Area(name='dongcheng')
# area2 = Area(name='chaoyang')
# session.add(area)
# session.add_all([area1, area2])
# session.commit()
# session.close()
print('**************')
#
# # 基础查询
# ret = session.query(Area).all()
# # get(id)
# ret1 = session.query(Area).get(1)
# # filter_by(字段)
# ret2 = session.query(Area).filter_by(name='chaoyang').first()
# # filter(表达式)
# ret3 = session.query(Area).filter(Area.name == 'dongcheng').first()
# print(ret1, ret2, ret3,  type(ret1), sep='\n',)
#
#
# # 删除
# session.query(Area).filter_by(id=26).delete()
# session.commit()
#
# # 修改
# session.query(Area).filter_by(id=27).update({'name': 'test'})
# session.query(Area).filter_by(id=27).update({Area.name: 'test1'})
# # 将默认的数据加减，改成字符串加减，默认synchronize_session=''evaluate'
# session.query(Area).filter_by(id=27).update({Area.name: Area.name + '~'}, synchronize_session=False)
# session.commit()
#
#
# # 常用操作
# # 条件查询
# ret1 = session.query(Area).filter_by(id=27).first()
# ret2 = session.query(Area).filter(Area.id < 3, Area.name == 'cangping').all()
# # between前包，后不包
# ret3 = session.query(Area).filter(Area.id.between(1, 3)).all()
# ret4 = session.query(Area).filter(~Area.id.in_([1, 2, 3])).first()
# ret5 = session.query(Area).filter(~(Area.id < 3)).first()
# print(ret2, ret3, ret4, sep='\n',)
#
# from sqlalchemy import and_, or_
# # 与或非
# # & |
# ret5 = session.query(Area).filter(and_(Area.id < 3, Area.name == 'cangping')).all()
# ret6 = session.query(Area).filter(or_(Area.id < 3, Area.name == 'cangping')).all()
# ret7 = session.query(Area).filter(or_(Area.id < 4, and_(Area.id < 3, Area.name == 'cangping'))).all()
# print(ret5, ret6, ret7, sep='\n',)
#
# # 通配符
# # c开头
# ret8 = session.query(Area).filter(Area.name.like("c%")).all()
# ret9 = session.query(Area).filter(~Area.name.like("c%")).all()
# print('ret8:', ret8, ret9, sep='\n',)
#
# # 切片
# ret10 = session.query(Area).filter(~Area.name.like("c%")).all()[1: 2]
# print('ret10:', ret10)
#
# # 分页
# ret11 = session.query(Area).limit(2).all()
# print('ret11:', ret11)
#
# ret12 = session.query(Area).limit(2).offset(1).all()  # 从第一条数据开始偏移1，
# # 即从第2条数据开始取
# print('ret12:', ret12)
#
# # 排序
# ret11 = session.query(Area).order_by(Area.name.desc()).all()
# ret12 = session.query(Area).order_by(Area.name).all()  # asc()默认
# # 多列排序
# ret13 = session.query(Area).order_by(Area.name.desc()).order_by(Area.id).all()
# print('ret13:', ret13)
# print('ret11:', ret11, ret12, ret13)
#
# # 分组
# ret13 = session.query(Area.name).group_by(Area.name).all()
# print('ret13:', ret13)
#
# # 聚合函数
# from sqlalchemy import func
# ret14 = session.query(func.max(Area.id), func.min(Area.id), func.sum(Area.id)).\
#     group_by(Area.name).all()
# ret15 = session.query(func.max(Area.id), func.min(Area.id), func.sum(Area.id)).\
#     group_by(Area.name).having(func.max(Area.id) > 30).all()
# print('ret14:', ret14, ret15, sep='\n')
#
# ret16 = session.query(Area.name, func.count(Area.name)).group_by(Area.name).all()
# ret16 = session.query(Area.name, func.count(Area.id)).group_by(Area.name).all()
# print('ret16:', ret16)
#
#
# print(session.query(func.max(Area.id)).first())  # (38,)
# print(session.query(func.max(Area.id)).one())  # (38,)  one前面的结果只能有一条
# print(session.query(func.max(Area.id)).scalar())  # 38 取one()的第一个元素
# print(session.query(Area).count())  # 17
#
#
# # 有条件的交叉联
# # 查询不同区域内的房子，4条数据（多对一）
# ret16 = session.query(Area, House).filter(Area.id == House.area_id).all()
# print('ret16:', ret16, type(ret16), sep='\n')
# # [(<Area 1>, <House 1>), (<Area 1>, <House 2>)，(<Area 2>, <House 1>), (<Area 2>, <House 2>)]
#
#
# # 内联 Inner Join
# # 2条数据
# # 通过Area的id和House的area_id相连，但是不用写出具体通过哪个键相连
# ret17 = session.query(Area).join(House).all()
# print('ret17:', ret17, sep='\n')
# for i in ret17:
#     print(i.id, i.name, i.houses)
#
# # [<Area 1>, <Area 2>]
# # 1 haidian [<House 1>, <House 2>]
#
#
# # 左联1
# ret18 = session.query(Area).all()
# print('ret18:', ret17, sep='\n')
# for i in ret18:
#     print(i.id, i.name, i.houses)
#
# # [<Area 1>, <Area 2>, <Area 23>]
# # 1 haidian [<House 1>, <House 2>]
# # 2 cangping [<House 3>, <House 4>]
# # 23 xicheng []
#
# # 左联2
# # Area数据全显示
# ret19 = session.query(Area).join(House, isouter=True).all()
# print('ret19:', ret19, sep='\n')
# for i in ret19:
#     print(i.id, i.name, i.houses)
#
# # [<Area 1>, <Area 2>, <Area 23>]
# # 1 haidian [<House 1>, <House 2>]
# # 2 cangping [<House 3>, <House 4>]
# # 23 xicheng []
#
# # 左联3
# ret20 = session.query(Area).outerjoin(House).all()
# print('ret20:', ret20, sep='\n')
# for i in ret20:
#     print(i.id, i.name, i.houses)
# # [<Area 1>, <Area 2>, <Area 23>]
# # 1 haidian [<House 1>, <House 2>]
# # 2 cangping [<House 3>, <House 4>]
# # 23 xicheng []
#
# # 右联
#
#
# # 4. 基于relationship的ForeignKey O2M
# # 基于relationship的反向查询
# area1 = session.query(Area).first()
# print(area1.id, area1.name)
# for i in area1.houses:
#     print(i.area_id)
#
#
# area2 = session.query(Area).join(House, Area.id == 1).all()
# area3 = session.query(Area, House).filter(Area.id == House.area_id, Area.id == 1).all()
# print('area3:', area3)
# print('area2:', area2)
# for a in area2:
#     print(a)
#     print(a.houses)
#     print(a)
#     print(a.houses[0].area_id)
#
#
# # 基于relationship的正向查询
# house1 = session.query(House).first()
# print(house1.id, house1.area_id,)

# # houses可能为空，即没有id字段
# for s in session.query(Area).filter(Area.houses.filter):# , Area.houses.id == 1
#     for ss in s.houses:
#         pass
# # for s in session.query(Area).filter(~(Area.id.is_(None))):
#     print(s.houses, type(s.houses), s.houses)





#
#
#
#
# print('====================')
# # 5. 基于relationship的ForeignKey M2M
# # 基于relationship的反向查询
# house = session.query(House).first()
# print(house.id, house.title, )
# print(house.facilities)
# # for i in house.facilities.house_facility:
# #     print(i)
#
# # house_facility=
#

#
# # 查询2号房子信息，及房子设施信息（多对多）
# print(house_facility.c.house_id)
#
# ret17 = session.query(House, house_facility).filter(House.id == house_facility.c.house_id).\
#     filter(House.id == 2).all()
# print('ret17:', ret17)
# for i in ret17:
#     print(i)
#
# a = session.query(House).join(house_facility, House.id == house_facility.c.house_id)
# print('a:', a)
#
# ret17 = session.query(House).join(house_facility, House.id == house_facility.c.house_id).filter(House.id == 2).all()
# print(ret17)
# ret20 = session.query(House).filter_by(id=1).first()
# print('20', ret20)
# print(ret20.facilities)
# print(ret20.orders)
# print(ret20.images)
#
#
#
#
#
#

# 在多对多表中添加数据
# Facility(id=4, name='cup'),
# session.add(Facility(id=5, name='light'))
# session.commit()
# session.close()

import jinja2
jinja2.Environment()
