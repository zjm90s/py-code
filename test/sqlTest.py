# -*- coding: utf-8 -*-
__author__ = 'zjm'

from main.z.db.datasource import DBSessions
from entity.family_entity import *


# run
session = DBSessions[User.DB_NAME]()
# user_list = session.execute('select * from family_agent where name = "zjm"').fetchall()
query = session.query(User).filter(User.name == "zjm")
user_list = query.all()
print query
print user_list
for user in user_list:
    print "{}:{}".format(user.id, user.name)
print "end"
