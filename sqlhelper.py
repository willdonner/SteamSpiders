from distutils import command

import logging2
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

            command =   'CREATE DATABASE IF NO EXISTS %s DEFAULT CHARACTER '