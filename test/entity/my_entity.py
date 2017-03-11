# -*- coding: utf-8 -*-
__author__ = 'zjm'

from sqlalchemy import Column,String
from sqlalchemy.ext.declarative import declarative_base

# ORM基类
Base = declarative_base()

class DB_Base():
    '''数据库级公共类

    由表级类继承
    '''

    # 数据库名称，对应resources/database.json中db_xxx
    DB_NAME = "db_test"


class User(Base, DB_Base):
    # 表名:
    __tablename__ = 'table'

    # 表结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

