#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from sqlalchemy.orm import mapper, sessionmaker

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.sql.expression import Cast
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

# #表的属性描述对象
metadata = MetaData()
userTable = Table(
     "user",metadata,
     Column('username', Integer, primary_key=True)
     )
     #,
#     Column('user_name', VARCHAR(50), unique=True, nullable=False),
#     Column('password', VARCHAR(40), nullable=True)
# )


# #创建数据库连接,MySQLdb连接方式
mysql_db = create_engine("mysql://root:imdb@219.228.147.36:3306/test")
# #创建数据库连接，使用 mysql-connector-python连接方式
 #mysql_db = create_engine("mysql+mysqlconnector://用户名:密码@ip:port/dbname")
#生成表
metadata.create_all(mysql_db)


# #创建一个映射类
class User(object):
     pass
# #把表映射到类
mapper(User, userTable)
# #创建了一个自定义了的 Session类
Session = sessionmaker()
# #将创建的数据库连接关联到这个session
Session.configure(bind=mysql_db)
session = Session()


def main():
    u = User()
    #给映射类添加以下必要的属性,因为上面创建表指定这个字段不能为空,且唯一
    #u.username=6
    #在session中添加内容
    #session.add(u)
    #保存数据
    #session.flush()
    #数据库事务的提交,sisson自动过期而不需要关闭
    #session.commit()



    #query() 简单的理解就是select() 的支持 ORM 的替代方法,可以接受任意组合的 class/column 表达式
    #query = session.query(User)
    #列出所有user
    # samplelist = list(query)
    # for element in samplelist:
    #     print element.username


    #print list(query)
    #根据主键显示
    #print query.get(1)
    #类似于SQL的where,打印其中的第一个
    #print query.filter_by(username='1').first()
    #u = query.filter_by(username='1').first()
    #print u.username


    #修改数据
    # u = query.filter_by(username='1').first()
    # u.username = '654321'
    #提交事务
    # session.commit()

    #删除数据
    #session.query(User).filter(User.username==0).delete()
    #session.commit()


    #根据username字段排序,打印其中的用户名
    # for instance in session.query(User).order_by(User.username):
    #     print instance.username
    #释放资源
    session.close()



if __name__ == '__main__':
     main()