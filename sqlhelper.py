from distutils import command

import logging
import mysql.connector
import utils
import config
from singleton import Singleton


class Sqlhelper(Singleton):
    def __init__(self):
        self.database_name = config.database_name
        self.inti()

    def inti(self):
        self.database = mysql.connector.connect(**config.database_config)
        self.cursor = self.database.cursor()

        self.create_database()
        self.database.database = self.database_name

    def create_database(self):
        try:
            command = 'CREATE DATABASE IF NO EXISTS %s DEFAULT CHARACTER \'utf8\'' % self.database_name
            utils.log('sql heler create_database command:%s' % command)
            self.cursor.execute(command)
        except Exception as e:
            utils.log('sql helper create_database Exception:%s' % str(e),
                      logging.warning('sql helper create_database Exception:%s' % str(e)))

    def create_table(self,command):
        try:
            utils.log('sql helper create_table command:%s'% command)
            self.cursor.execute(command)
            self.database.commit()
        except Exception as e:
            utils.log('sql helper create_table Exception:%s' % str(e)),
            logging.warning('sql helper create_table Exception:%s' % str(e))

    def insert_data(self, command):
        try:
            self.cursor.execute(command)
            self.database.commit()
        except Exception as e:
            utils.log('sql helper insert_data Exception:%s' % str(e)),
            logging.warning('sql helper insert_data Exception:%s' % str(e))

    def execute(self, command):
        try:
            utils.log('sql helper execute command:%s' % command)
            data = self.cursor.execute(command)
            self.database.commit()
            return data
        except Exception as e:
            utils.log('sql helper execute exception msg:%s' % str(e))
            return None

    def query(self, command): #查询全部
        try:
            utils.log('sql helper execute command:%s' % command)

            self.cursor.execute(command)
            data = self.cursor.fetchall()

            return data
        except Exception as e:
            utils.log('sql helper execute exception msg:%s' % str(e))
            return None

    def query_one(self, command): #查询一条
        try:
            utils.log('sql helper execute command:%s' % command)

            self.cursor.execute(command)
            data = self.cursor.fetchone()

            return data
        except Exception as e:
            utils.log('sql helper execute exception msg:%s' % str(e))
            return None
