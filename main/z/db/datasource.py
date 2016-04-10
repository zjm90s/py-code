# -*- encoding:utf-8 -*-
__author__ = 'zjm'

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from res_init import res_path

# DBSession集合
DBSessions = dict()


def __init_datasource():
    """初始化数据库连接

    根据resources/database.json初始化，session置于全局DBSessions中
    """
    databases = json.load(file(res_path("database.json")))
    for database in databases:
        db_url = ("mysql+pymysql://{user}:{passwd}@{host}:{port}/{database}?charset=utf8"
                  .format(**databases[database]))
        engine = create_engine(db_url)
        # 创建DBSession类型
        DBSessions[database] = scoped_session(sessionmaker(bind=engine))


# init
__init_datasource()
