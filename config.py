# !usr/bin/env python
# -*- encoding=utf8 -*-

"""
配置文件，配置flask框架的各种设置，数据库的设置
"""

# 调试模式
DEBUG = True

# 数据库类型
DIALECT = 'mysql'
# 数据驱动
DRIVER = 'mysqlconnector'
# 数据库用户名
USERNAME = 'root'
# 数据库密码
PASSWORD = ''
# 数据库地址
HOST = '127.0.0.1'
# 数据库端口
PORT = '3306'
# 数据库名称
DB = 'shoa'
# 数据库URI(dialect + driver://username:password@host:port/database?charset)
SQLALCHEMY_DATABASE_URI = '%s+%s://%s:%s@%s:%s/%s?charset=utf8' % \
                          (DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DB)

# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = False
