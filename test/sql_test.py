# -*- coding: utf-8 -*-
__author__ = 'zjm'

import MySQLdb
import pymysql
import torndb
import pytorndb


def mysqldb_test():
    db = MySQLdb.connect(host = "localhost", port = 3306, user = "zjm", passwd = "654321", db = "my_db")
    cursor = db.cursor()
    cursor.execute("select * from my_table")
    result = cursor.fetchone();
    print result
    cursor.execute("select * from my_table")
    results = cursor.fetchall()
    print results
    cursor.close()
    db.close()


def pymysql_test():
    db = pymysql.connect(host = "localhost", port = 3306, user = "zjm", passwd = "654321", db = "my_db")
    cursor = db.cursor()
    cursor.execute("select * from my_table")
    result = cursor.fetchone();
    print result
    cursor.execute("select * from my_table")
    results = cursor.fetchall()
    print results
    cursor.close()
    db.close()


def torndb_test():
    db = torndb.Connection("localhost:3306", "my_db", user="zjm", password="654321")
    rel = db.get("select * from my_table limit 1")
    print rel
    rels = db.query("select * from my_table")
    print rels
    db.close()


def pytorndb_test():
    db = pytorndb.Connection("localhost:3306", "my_db", user="zjm", password="654321")
    rel = db.get("select * from my_table limit 1")
    print rel
    rels = db.query("select * from my_table")
    print rels
    db.close()


torndb_test()